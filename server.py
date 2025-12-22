from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# IMPORT DAS ROTAS DEPOIS DO APP EXISTIR
import auth.route

if __name__ == '__main__':
    app.run(debug=True)
