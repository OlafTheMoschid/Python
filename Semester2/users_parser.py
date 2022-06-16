from flask_restful import reqparse

parser = reqparse.RequestParser()

parser.add_argument('nickname', required=False)
parser.add_argument('email', required=False)
parser.add_argument('hashed_password', required=False)
