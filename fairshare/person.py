from flask import (
    Blueprint, render_template, request, flash, abort, redirect, url_for
)

from fairshare.auth import login_required
from fairshare.db import get_db

bp = Blueprint('person', __name__, url_prefix='/person')


@bp.route('/new', methods=('GET', 'POST'))
@login_required
def new():
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Name is requried'

        if error is None:
            db = get_db()
            db.execute(
                "INSERT INTO person (name) VALUES (?)",
                (name,)
            )
            db.commit()
            return redirect(url_for('person.index'))

        flash(error)
    return render_template('person/new.html')


@bp.route('/edit', methods=('POST', ))
@login_required
def edit():
    id = request.args['id']

    if len(request.form) >= 1:
        name = request.form['name']
        error = None

        if not name:
            error = 'Name can not be empty!'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE person SET name = ?'
                ' WHERE id = ?',
                (name, id)
            )
            db.commit()
            return redirect(url_for('person.index'))

    person = get_person(id)
    return render_template('person/edit.html', person=person)


def get_person(id):
    person = get_db().execute(
            'SELECT id, name FROM person WHERE id = ?',
            (id,)
        ).fetchone()

    if person is None:
        abort(404, f"Person with id {id} does not exist!")

    return person


@bp.route('/')
@login_required
def index():
    db = get_db()
    persons = db.execute(
        'SELECT name, id'
        ' FROM person'
    ).fetchall()
    return render_template('person/index.html', persons=persons)


@bp.route('/delete', methods=('POST',))
@login_required
def delete():
    id = request.args['id']
    db = get_db()
    db.execute(
        'DELETE FROM person'
        ' WHERE id = ?',
        (id,)
    )
    db.commit()
    return redirect(url_for('person.index'))
