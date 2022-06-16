import datetime
import hashlib

from flask import Blueprint, jsonify, request
from data import db_session
from data.users import User

blueprint = Blueprint('user_api', __name__,
                      template_folder='templates')


@blueprint.route('/api/users')
def get_users():
    session = db_session.create_session()
    users = session.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('nickname', 'email'))
                 for item in users]
        }
    )


@blueprint.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user_id = int(user_id)
    except:
        return jsonify({'error': 'Bad request: Id type must be integer'})

    users_id = []
    session = db_session.create_session()
    users = session.query(User)
    for i in users:
        users_id.append(i.id)
    if user_id not in users_id:
        return jsonify({'error': 'Bad request: Id does not exist'})

    user = session.query(User).filter(User.id == user_id).first()
    return jsonify(
        {
            'user':
                user.to_dict(only=('nickname', 'email'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def add_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    if type_checks():
        return jsonify({'error': 'Bad request: Wrong data type'})
    elif not all(key in request.json for key in
                 ['nickname', 'email', 'password']):
        return jsonify({'error': 'Bad request: Not enough data'})

    session = db_session.create_session()
    if session.query(User).filter(User.email == request.json['email']).first():
        return jsonify({'error': 'User you`ve entered already exists'})

    user = User(
            nickname=args['nickname'],
            email=args['email'],
            hashed_password=user.set_password(args['hashed_password'])
        )

    session.add(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user_id = int(user_id)
    except:
        return jsonify({'error': 'Bad request: Id type must be integer'})

    users_id = []
    session = db_session.create_session()
    users = session.query(User)
    for i in users:
        users_id.append(i.id)
    if user_id not in users_id:
        return jsonify({'error': 'Bad request: Id does not exist'})

    user = session.query(User).filter(User.id == user_id).first()

    session.delete(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<user_id>', methods=['POST'])
def change_user(user_id):
    try:
        user_id = int(user_id)
    except:
        return jsonify({'error': 'Bad request: Id type must be integer'})

    users_id = []
    session = db_session.create_session()
    users = session.query(User)
    for i in users:
        users_id.append(i.id)
    if user_id not in users_id:
        return jsonify({'error': 'Bad request: Id does not exist'})
    if not request.json:
        return jsonify({'error': 'Empty request'})
    if type_checks():
        return jsonify({'error': 'Bad request: Wrong data type'})
    if request.json.get('email', None):
        if session.query(User).filter(User.email == request.json['email']).first():
            return jsonify({'error': 'User you`ve entered already exists'})

    user = session.query(User).filter(User.id == user_id).first()
    if request.json.get('nickname', None):
        user.name = request.json['nickname']
    if request.json.get('email', None):
        user.email = request.json['email']
    if request.json.get('password', None):
        user.set_password(request.json['password'])

    session.commit()
    return jsonify({'success': 'OK'})


def type_checks():
    nickname_type = type(request.json.get('name', None))
    email_type = type(request.json.get('email', None))
    password_type = type(request.json.get('password', None))

    if nickname_type is not str and nickname_type is not type(None):
        return True
    if email_type is not str and email_type is not type(None):
        return True
    if password_type is not str and password_type is not type(None):
        return True
    return False
