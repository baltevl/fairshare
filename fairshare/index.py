from flask import (
    Blueprint, render_template
)

from fairshare.auth import login_required

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
@login_required
def index():
    return render_template('index/index.html')
