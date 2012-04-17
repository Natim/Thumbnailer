ROOT_DIR=$(PWD)

runserver: static_serveur provider_server

test: static_server provider_server
	cd $(ROOT_DIR)/tests; lettuce

static_server:
	cd $(ROOT_DIR)/static; python -m SimpleHTTPServer &

provider_server:
	cd $(ROOT_DIR)/flask_thumbnailer; python provider.py &

