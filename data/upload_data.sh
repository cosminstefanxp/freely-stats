#!/bin/bash
if [ $# -lt 2 ]
then
	echo "***ERROR***"
    echo "Usage : $0 kind filename <remote>"
    exit
fi

case "$3" in 
	"remote")
	echo "Uploading data to remote server..."
	 ~/.appengine_python/appcfg.py --email=cosminstefanxp@gmail.com upload_data --config_file=bulkloader.yaml --filename="$2" --kind="$1" --url='http://freelystats.appspot.com/_ah/remote_api'
	;;
	*)
	echo "Uploading data to local server..."
	~/.appengine_python/appcfg.py upload_data --config_file=bulkloader.yaml --filename="$2" --kind="$1" --url='http://localhost:8080/_ah/remote_api'
	;;
esac
