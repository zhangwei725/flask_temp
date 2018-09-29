from flask import Flask

from apps.ext import init_ext
from apps.main.views import main
from apps.temp.views import temp

# 80行  按着作用拆分成函数
from apps.temp.filter import format_date
from apps.upload.views import upload


def init_filter(app):
    app.add_template_filter(format_date, 'datetime')


def init_blue(app):
    app.register_blueprint(temp)
    app.register_blueprint(main)
    app.register_blueprint(upload)


def create_app():
    app = Flask(__name__)
    app.debug = True
    init_filter(app)
    init_blue(app)
    init_ext(app)
    return app
