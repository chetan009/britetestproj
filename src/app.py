#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from frequest import app


if __name__ == '__main__':
    if not os.path.exists(app.config['DB_FILE']):
        app.db.create_all()

    app.debug = True
    app.run(host='0.0.0.0', port=80, debug=True)
