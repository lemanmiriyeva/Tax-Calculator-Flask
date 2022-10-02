
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "Products"

from controllers import *

if __name__=='__main__':
    app.run(port=5000,debug=True)