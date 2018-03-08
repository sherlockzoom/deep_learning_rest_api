# coding=utf-8
# --------------------------
# @Time    : 18-2-8 上午10:47
# @Author  : knight
# @File    : keras_rest_api_app.wsgi.py
# --------------------------
# import sys
# sys.path.insert(0, '/home/knight/ToT/deep_learning_rest_api/app')

from app.run_web_server import app as application

if __name__ == '__main__':
    application.run()