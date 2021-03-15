#!/bin/bash
source /home/www/web-site/extension-env/bin/activate
exec gunicorn -c '/home/www/web-site/extension-backend/gunicorn_config.py' config.wsgi
