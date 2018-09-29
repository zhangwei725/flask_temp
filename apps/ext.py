from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class


def init_ext(app):
    # 初始化数据库
    init_db(app)
    # 文件上传初始化
    init_uploads(app)


# orm框架配置
db = SQLAlchemy()
migrate = Migrate()


# ctrl+shift + u  大小写切换

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/temp'
    db.init_app(app)
    migrate.init_app(app, db)


# =======文件上传相关配置 start======
# 配置路径
import os

# 获取当前文件所有在根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 获取当前跟目录下文件上传的目录
UPLOAD_PATH = os.path.join(BASE_DIR, 'static/upload/')
# 文件上传核心类
images_upload = UploadSet('images', extensions=IMAGES)


# files = UploadSet()


def init_uploads(app):
    # 配置文件上传的根目录
    app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_PATH
    app.config['UPLOADS_DEFAULT_URL'] = 'http://127.0.0.1:5000/static/upload'
    #     配置文件上传的类型
    configure_uploads(app, images_upload)
    # 配置上传文件的最大值
    patch_request_class(app, 16 * 1024 * 1024)

# =======文件上传相关配置 end======
