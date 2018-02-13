# -*- coding: utf-8 -*-
from logging.handlers import RotatingFileHandler

from flask import logging

from web import app

if __name__ == "__main__":
    handler = RotatingFileHandler('web.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    handler.setLevel(logging.DEBUG)
    logger = logging.getLogger('tdm')
    app.logger.addHandler(handler)
    app.debug = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(threaded=True)

