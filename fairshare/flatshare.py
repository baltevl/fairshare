from flask import (
    Blueprint, render_template, request, flash
)

from fairshare.auth import login_required
from fairshare.db import get_db

bp = Blueprint('flatshare', __name__, url_prefix='/flatshare')


@bp.route('/new')
@login_required
def new():
    return render_template('flatshare/new.html')


@bp.route('/edit')
@login_required
def edit():
    return render_template('flatshare/edit.html')
