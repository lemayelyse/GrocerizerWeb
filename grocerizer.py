from grocerapp import app, db
from grocerapp.dbhelper import Grocery

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Groceries': Grocery}