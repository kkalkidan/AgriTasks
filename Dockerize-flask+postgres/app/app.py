from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, text
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test:test@db/test"
db = SQLAlchemy(app)
# the database needs to be formated like this and exported
# export DATABASE_URL="postgresql://{username}@localhost/{databasename}"

migrate = Migrate(app, db)
@app.route('/')
def index():
    return "This page is under construction :)"

@app.route('/accounts/', methods=['GET'])
def create_user():
    db.create_all()
    new_id = request.args.get('id', default=1, type=str)
    from models import Account
    new_account = Account(id=new_id)
    db.session.add(new_account)
    db.session.commit()
    return "Accout with account id " + new_id + " created"

@app.route('/list_accounts/', methods=['GET'])	
def list_accounts():
    sql = text('select * from account')
    result = db.engine.execute(sql).fetchall()
    return str(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
