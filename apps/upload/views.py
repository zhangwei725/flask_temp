from flask import Blueprint, request, render_template, jsonify

from apps.ext import images_upload
from apps.upload.helper import get_new_file_name

upload = Blueprint('upload', __name__)


# 请求方式 必须是post 或者put  而且数据格式类型必须是 formdata

@upload.route('/uploads/', methods=['post', 'put', 'get'])
def upload_img():
    if request.method == 'GET':
        return render_template('upload/upload.html')
    elif request.method in ['POST', 'PUT']:
        file_store = request.files.get('img')
        name = images_upload.save(file_store, name=get_new_file_name(file_store.filename))
        url = images_upload.url(name)
        return url


@upload.route('/upload/ajax/', methods=['post'])
def upload_ajax():
    username = request.values.get('username')
    password = request.values.get('password')
    file_store = request.files.get('img')
    name = images_upload.save(file_store, name=get_new_file_name(file_store.filename))
    # 返回图片访问的地址
    url = images_upload.url(name)
    result = {
        'status': 200,
        'msg': 'upload success',
        'url': url
    }
    return jsonify(result)
