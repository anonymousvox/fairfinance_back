import flask
from flask import abort
from flask_restx import Namespace, Resource, fields
from models.model_user import User, db
from sqlalchemy.exc import IntegrityError
from action.notification_user import NotificationUser
from action.generate_password import generate_password
from constant import user_constant
import hashlib

api = Namespace('auth', description='Auth user service', path='/registration')


class RegistrationResponseDto:
    
    user = api.model('user', {
        'id': fields.Integer(description='User Identifier'),
        'phone': fields.String(description='User login'),
        'email': fields.String(description='User email')
    })

    user_full_registration = api.model('user_full_registration', {
        'id': fields.Integer(description='Id user')
    })


class RegistrationRequestDto:

    user_create = api.model('user_create',{
        'name': fields.String(description='User name'),
        'phone': fields.String(description='User login'),
        'email': fields.String(description='User email')
    })

    user_full_registration = api.model('user_full_registration', {
        'user_id': fields.Integer(description='Id user', ),
        'fio': fields.String(description='User FIO'),
        'inn': fields.Integer(description='User INN'),
        'snils': fields.String(description='User snils'),
        'birth_date': fields.DateTime(description='User birth_date'),
        'birth_place': fields.String(description='User birth_place'),
        'passport_series': fields.String(description='User passport_series'),
        'passport_date_of_issue': fields.Date(description='User passport_series'),
        'passport_division_code': fields.String(description='User passport_series'),
        'passport_division_name': fields.String(description='User passport_series'),
        'registration_address': fields.String(description='User passport_series'),
        'living_address': fields.String(description='User passport_series'),
        'pass_scan': fields.String(description='User passport_series'),
        'pass_registration_scan': fields.String(description='User passport_series'),
    })
    

@api.route('', methods=['GET', 'POST', 'PUT', 'DELETE'])
class UserAuth(Resource):

    @api.doc('Get All user test TODO: delete')
    @api.marshal_list_with(RegistrationResponseDto.user)
    def get(self):
        user = User.query.all()
        return user
    
    @api.doc('Registration new user in platform')
    @api.expect(RegistrationRequestDto.user_create)
    @api.marshal_list_with(RegistrationResponseDto.user)
    def post(self):
        try:
            password = generate_password()
            password_hash_md5 = hashlib.md5(password.encode()).hexdigest()
            api.payload['password'] = password_hash_md5
            user: User = User(**api.payload)
            db.session.add(user)
            db.session.commit()
            message_text = user_constant.WELCOME_PLATFORM.format(password=password_hash_md5)
            notification_user = NotificationUser(user.phone, user.email, user_constant.REGISTRATION_USER,
                                                 message_text)
            notification_user()
            return user, 201
        except IntegrityError as e:
            db.session.rollback()
            return abort(400, "User with login already exists")
        except Exception as e:
            db.session.rollback()
            return abort(400, "Failed register user")


@api.route('/full', methods=['POST'])
class FullRegistration(Resource):
    @api.doc('')
    @api.expect(RegistrationRequestDto.user_full_registration)
    @api.marshal_list_with(RegistrationResponseDto.user_full_registration)
    def post(self):
        #TODO: add varification pass and inn and check stop factor user
        pass
