from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
import read_from_1c as rfc


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/sn/')
def sn():
    data = rfc.read_data()
    my_response = make_response(data)
    my_response.mimetype = "application/json"
    my_response.status_code = 200
    return my_response

if __name__ == '__main__':
    app.run(debug=True)