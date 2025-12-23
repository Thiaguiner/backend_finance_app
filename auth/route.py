from flask import request, Flask, Blueprint
from .controller import AuthController


auth_bp = Blueprint('auth', __name__, template_folder='templates')
@auth_bp.post('/login')
def login():
    data = request.get_json()
    print('DATA RECEBIDA:', data)

    return AuthController().loggin_controller(data.get('login'),data.get('senha'))

@auth_bp.post('/cadastro')
def cadastro():
    data = request.get_json()
    print('DATA RECEBIDA:', data)

    return AuthController().cadastro_controller(data.get('nome'),data.get('senha'), data.get('email'))
