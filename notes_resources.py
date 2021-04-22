from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from data import db_session, Notes, User
from flask_restful import Resource
from datetime import datetime

parser = reqparse.RequestParser()
parserd = reqparse.RequestParser()
parser.add_argument('content', required=True, type=str)
parser.add_argument('api_key', required=True, type=str)
parserd.add_argument('api_key', required=True, type=str)


class NotesResource(Resource):
    def get(self, notes_id):
        abort_if_news_not_found(notes_id)
        session = db_session.create_session()
        note = session.query(Notes).get(notes_id)
        return jsonify({'note': note.to_dict(
            only=('id', 'content', 'user_id', 'created_date'))})

    def delete(self, notes_id):
        args = parserd.parse_args()
        abort_if_news_not_found(notes_id)
        session = db_session.create_session()
        abort_if_invalid_api_key(session, args)
        notes = session.query(Notes).get(notes_id)
        session.delete(notes)
        session.commit()
        return jsonify({'success': 'OK'})


class NotesListResource(Resource):
    def get(self):
        session = db_session.create_session()
        notes = session.query(Notes).all()
        return jsonify({'notes': [item.to_dict(
            only=('id', 'content', 'user.name', 'created_date')) for item in notes]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        abort_if_invalid_api_key(session, args)
        notes = Notes(
            content=args['content'],
            user_id=1,
            created_date=datetime.now()
        )
        session.add(notes)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_news_not_found(note_id):
    session = db_session.create_session()
    notes = session.query(Notes).get(note_id)
    if not notes:
        abort(404, message=f"Note {note_id} not found")


def abort_if_invalid_api_key(session, args):
    secret_key = session.query(User).get(1).hashed_password
    api_key = args['api_key']
    if secret_key != api_key:
        abort(403, message=f'Invalid api key:{secret_key}')