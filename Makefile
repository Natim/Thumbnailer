ROOT_DIR=$(PWD)
STATIC_PID_FILE=run/static_server.pid
PROVIDER_PID_FILE=run/provider_server.pid
VIRTUALENV=virtualenv

test: runserver
	sleep 2
	cd $(ROOT_DIR)/tests; lettuce

runserver: kill_server static_server provider_server

static_server:
	cd $(ROOT_DIR)/static; python -m SimpleHTTPServer & echo "$$!" > ../$(STATIC_PID_FILE)

provider_server:
	python run.py & echo "$$!" > $(PROVIDER_PID_FILE)

kill_server:
#Kill server and child processus
	for PID in `cat $(STATIC_PID_FILE) $(PROVIDER_PID_FILE)`; do \
	  PPID=`ps -ef | awk '$$3 == '$${PID}' { print $$2 }'`;\
	  if [ '$${PID}' != '' ]; then kill $${PID};\
	    for ppid in $${PPID}; do kill $${ppid}; done;\
	  fi;\
	done
	-rm -f $(STATIC_PID_FILE) $(PROVIDER_PID_FILE)

install: virtualenv upgrade develop
	mkdir -p var/input var/thumbs

virtualenv:
	if [ ! -f $(PYTHON) ]; then \
            if [[ "`$(VIRTUALENV) --version`" < "`echo '1.8'`" ]]; then \
                $(VIRTUALENV) --no-site-packages --distribute env; \
            else \
                $(VIRTUALENV) env; \
            fi \
        fi

upgrade:
	env/bin/pip install -r requirements.pip

develop:
	(cd src/thumbnailer.core/; ../../env/bin/python setup.py develop)
	(cd src/thumbnailer.engines.documents/; ../../env/bin/python setup.py develop)
	(cd src/thumbnailer.engines.images/; ../../env/bin/python setup.py develop)
