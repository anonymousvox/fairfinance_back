
from flask_restx import Namespace, Resource
from config.user_config import PATH_SAVE_FILE
from flask import request
import uuid
import os

api = Namespace('auth', description='Auth user service', path='/fileuploads')

@api.route('/', methods=['POST'])
class FileUploads(Resource):

    @api.doc("upload file")
    def post(self):
        try:
            os.makedirs(PATH_SAVE_FILE, exist_ok=True)
            user_id = request.args.get('user_id')
            file = request.files['file']
            if file:
                filename = "".join([str(uuid.uuid4()), '.', file.filename.rsplit('.', 1)[1].lower()])
                filepath = "".join([PATH_SAVE_FILE, filename])
                file.save(filepath)
                return {"file_name": filename}, 200
        except Exception as e:
            return {"error": "FILE", "errorMessage": "Incorrect format"}, 400