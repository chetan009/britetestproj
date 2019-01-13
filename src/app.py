#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import os
import sys
import logging
from frequest import app


if __name__ == '__main__':
    sys.getfilesystemencoding = lambda: 'UTF-8'
    #if not os.path.exists(app.config['LOG_DIR']):
    #    os.makedirs(app.config['LOG_DIR'])

    #if not os.path.exists(app.config['PID_DIR']):
    #    os.makedirs(app.config['PID_DIR'])

    #handler = logging.handlers.RotatingFileHandler('frequest_app.log',
    #                                               maxBytes=1000,
    #                                               backupCount=5)
    #handler.setLevel('DEBUG')
    #app.logger.addHandler(handler)
    if not os.path.exists(app.config['DB_FILE']):
        app.db.create_all()

    app.debug = True
    app.run(host='0.0.0.0', port=80, debug=True)