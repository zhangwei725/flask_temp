# 给文件重名了
import datetime

SUFFIX_IMG = 'IMG'


def get_new_file_name(filename):
    # 文件名+ 后缀  IMG201809.JPG
    suffix_name = '.' + filename.split('.')[-1]
    prefix_name = SUFFIX_IMG + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return prefix_name + suffix_name
