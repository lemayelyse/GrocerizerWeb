from flask import render_template, flash, redirect, url_for
from grocerapp import app, db
from grocerapp.forms import AddToListForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Elyse'}
    return render_template('index.html', title='Home', user=user)


@app.route('/additem', methods=['GET', 'POST'])
def additem():
    form = AddToListForm()
    if form.validate_on_submit():
        db.add_kw(form.item.data)
        flash('Item added: {}'.format(form.item.data))
    return render_template('additem.html', title='Add Item', form=form)

@app.route('/view')
def view():
    data = db.query()

    return render_template('view.html', data=data)
