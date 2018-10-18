from flask import render_template, flash, redirect, url_for
from grocerapp import app
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
        flash('Item added: {}'.format(form.item.data))
        return redirect(url_for('index'))
    return render_template('additem.html', title='Add Item', form=form)
