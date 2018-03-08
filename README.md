# keras-flask-nginx-uwsgi 部署参考

1. 安装依赖`pip install -r requirements.txt`
2. 配置uwsgi_config.ini
3. load model `python app/run_model_server.py`
3. run  `uwsgi --ini uwsgi_config.ini`


参考： https://www.pyimagesearch.com/2018/02/05/deep-learning-production-keras-redis-flask-apache/