from flask import Flask
from orm import User
import os
app = Flask(__name__)
base_dir = '/'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

db = User(app)




@app.route("/")
def index():
    return "hello S17"

if __name__ == '__main__':
    app.run()