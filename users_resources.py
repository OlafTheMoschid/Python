from flask import jsonify
from flask_restful import Resource, reqparse
from data import db_session
from data.users import User
from werkzeug.security import generate_password_hash
import users_parser


def check_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return True
    return False


class UsersResource(Resource):
    def get(self, user_id):
        try:
            user_id = int(user_id)
        except:
            return jsonify({'error': 'Bad request: Id type must be integer'})

        if check_user_not_found(user_id):
            return jsonify({'error': 'Bad request: Id does not exist'})

        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify(
            {
                'user':
                    user.to_dict(only=('nickname', 'email'))
            }
        )

    def post(self, user_id):
        args = users_parser.parser.parse_args()
        try:
            user_id = int(user_id)
        except:
            return jsonify({'error': 'Bad request: Id type must be integer'})

        if check_user_not_found(user_id):
            return jsonify({'error': 'Bad request: Id does not exist'})
        if args['email']:
            if session.query(User).filter(User.email == args['email']).first():
                return jsonify({'error': 'User you`ve entered already exists'})

        session = db_session.create_session()
        user = session.query(User).filter(User.id == user_id).first()

        if args['nickname']:
            user.nickname = args['nickname']
        if args['email']:
            user.email = args['email']
        if args['password']:
            user.set_password(args['hashed_password'])

        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        try:
            user_id = int(user_id)
        except:
            return jsonify({'error': 'Bad request: Id type must be integer'})
        if check_user_not_found(user_id):
            return jsonify({'error': 'Bad request: Id does not exist'})

        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify(
            {
                'users':
                    [item.to_dict(only=('nickname', 'email'))
                     for item in users]
            }
        )

    def post(self):
        args = users_parser.parser.parse_args()
        if not args:
            return jsonify({'error': 'Empty request'})
        for i in args.keys():
            if args[i] is None:
                return jsonify({'error': 'Bad request: Not enough data'})

        session = db_session.create_session()
        if session.query(User).filter(User.email == args['email']).first():
            return jsonify({'error': 'User you`ve entered already exists'})

        user = User(
            nickname=args['nickname'],
            email=args['email'],
            hashed_password=generate_password_hash(args['hashed_password'])
        )

        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
