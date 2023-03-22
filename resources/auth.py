from flask import abort
from flask_restx import Namespace, Resource, fields
from models.model_user import User, db
from sqlalchemy.exc import IntegrityError
from action.get_password_platform import GetPasswordPlatform
import hashlib

api = Namespace('auth', description='Auth user service', path='/auth')


class RegistrationResponseDto:
    user = api.model('user', {
        'id': fields.String(description='User Identifier'),
        'phone': fields.String(description='User login'),
        'email': fields.String(description='User email')
    })

class AuthRequestDto:
    user_auth = api.model('user_auth', {
        'phone': fields.String(description='User login'),
        'password': fields.String(description='User password')
    })


@api.route('', methods=['GET', 'POST', 'PUT', 'DELETE'])

class UserAuth(Resource):

    @api.doc('')
    @api.expect(AuthRequestDto.user_auth)
    @api.marshal_list_with(RegistrationResponseDto.user)
    def post(self):
        try:
            password = api.payload.get('password')
            phone = api.payload.get('phone')
            get_password_password = GetPasswordPlatform(password=password)
            password_hash_md5 = get_password_password.get()
            user = User.query.filter_by(phone=phone).filter_by(password=password_hash_md5).first()
            return user, 201
        except IntegrityError as e:
            db.session.rollback()
            return abort(400, "User with login already exists")
        except Exception as e:
            db.session.rollback()
            return abort(400, "Failed register user")