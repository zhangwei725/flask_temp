from flask import Blueprint, render_template, request

from apps.temp.models import Travel

main = Blueprint('main', __name__)


# /main/list/1/10/
# /main/list/?page=1&size=10
@main.route('/main/list/')
def list():
    page = request.values.get('page', default=1, type=int)
    per_page = request.values.get('size', default=10, type=int)
    paginate = Travel.query.order_by(Travel.create_date).paginate(page=page, per_page=per_page, error_out=False)
    # html_msg = render_template('mail.html')
    return render_template('page1.html', paginate=paginate)
