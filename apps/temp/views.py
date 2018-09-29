import datetime

from flask import Blueprint, render_template, url_for

from apps.ext import db
from apps.temp.models import Travel

temp = Blueprint('temp', __name__)


# app新建 templatetags
# mvc

@temp.route('/')
def index():
    li = [1, 2, 3]
    now = datetime.datetime.now()
    return render_template('index.html', now=now, li=li)


@temp.route('/add/')
def add():
    travels = []
    for i in range(1, 101):
        if i % 2 == 0:
            travels.append(Travel(title=f'气质{i}'))
        else:
            travels.append(Travel(title=f'明星{i}'))
    db.session.add_all(travels)
    db.session.commit()
    return '添加成功'


# 字段
# 方法
# 属性
@temp.route('/list/<int:page>/<int:size>/')
def list(page, size):
    # 执行函数
    """
    :param page: 页数
    :param per_page: 每页多少条
    :error_out  True 404   False 返回最后一页:
    """
    paginate = Travel.query.paginate(page=page, per_page=size, error_out=False)

    # pagnigate对象
    """
    字段
    page 当前是第一页
    per_page 每页多少条
    total 总共条数据
    items 当前页的数据
    属性 
    prev 上一页
    next 下一页
    pages 总页数
    has_prev 是否有上一页
    has_next  是否有下一页
    方法
    iter_pages() 返回分页显示的页码
    参数说明
    left_edge=2,  最左边最少默认显示2条数据
    left_current=2, 当前页左边显示多少条数据 默认2
    right_current=5, 当前页右边显示多少条数据 默认5
    right_edge=2   最右边最少默认显示2条数据
    注意 当前超过10条的时候 中间的页面默认使用none代替
    """
    # 字段
    # 方法
    # 属性
    # 声明的时候是函数
    # 使用的是变量
    #
    # paginate.pages  总页数
    # paginate.has_next
    # left = 5
    # right = 5
    # if page < 6:
    #     right = 11 - page
    # elif paginate.pages - page < 5:
    #     left = 9 - (paginate.pages - page)

    # paginate.iter_pages(left_edge=0, left_current=5,
    #                     right_current=5, right_edge=0)

    return render_template('page.html', paginate=paginate)


@temp.route('/pages/')
def page():
    print(url_for('.list', page=1, size=5))

    return render_template('temp1.html')


