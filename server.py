from flask import Flask, Blueprint
from flask_cors import CORS
from auth.route import auth_bp

app = Flask(__name__)

CORS(app, supports_credentials=True)


app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
