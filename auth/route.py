from flask import request
from server import app
from .controller import AuthController


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print('DATA RECEBIDA:', data)

    return AuthController().loggin_controller(
        data.get('login'),
        data.get('senha')
    )
