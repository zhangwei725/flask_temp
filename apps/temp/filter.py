# 自定义过滤器
# 变量或者值|过滤器的名称()


import datetime


# 自定义过滤器本质是一个函数
# 第一步定义函数
# 第二歩根据业务需求处理值,返回处理后的值
# 注册自定义过滤器
# 1>装饰器  @app.template_filter('datetime')
# 2> app.add_template_filter(函数名,'使用的别名')
# 注意
# 1> 过滤器必须有返回值
# 2> 过滤器的第一个参数是需要处理的值


# @app.template_filter('datetime')
def format_date(value, format='%Y-%m-%d %H:%M:%S'):
    if isinstance(value, datetime.datetime) or isinstance(value, datetime.date):
        return datetime.datetime.strftime(value, format)
    else:
        return value

