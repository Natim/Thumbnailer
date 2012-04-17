ROOT_DIR=$(PWD)
STATIC_PID_FILE=run/static_server.pid
PROVIDER_PID_FILE=run/provider_server.pid

test: runserver
	sleep 1
	cd $(ROOT_DIR)/tests; lettuce

runserver: kill_server static_server provider_server

static_server:
	cd $(ROOT_DIR)/static; python -m SimpleHTTPServer & echo "$$!" > ../$(STATIC_PID_FILE)

provider_server:
	cd $(ROOT_DIR)/thumbnailer; python provider.py & echo "$$!" > ../$(PROVIDER_PID_FILE)

kill_server:
#Kill server and child processus
	for PID in `cat $(STATIC_PID_FILE) $(PROVIDER_PID_FILE)`; do \
	  PPID=`ps -ef | awk '$$3 == '$${PID}' { print $$2 }'`;\
	  if [ '$${PID}' != '' ]; then kill $${PID};\
	    for ppid in $${PPID}; do kill $${ppid}; done;\
	  fi;\
	done
	-rm -f $(STATIC_PID_FILE) $(PROVIDER_PID_FILE)
