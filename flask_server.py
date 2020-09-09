from flask import Flask, Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

from Python.src.data_extraction import DataExtraction
from Python.src.request import Request
from Python.src.text_similarity import DocumentSimilarity


def flask_server():
    app = Flask(__name__)
    auth = HTTPBasicAuth()

    users = {
        "Norway": generate_password_hash("Hallo"),
    }

    @auth.verify_password
    def verify_password(username, password):
        if username in users and check_password_hash(users.get(username), password):
            return username

    @app.route('/v.0.1/getApartmentParameters', methods=['POST'])
    @auth.login_required
    def get_params():
        init_request = Request()
        text = init_request.get_text()
        data = init_request.get_data()
        model_name = init_request.get_model_name()
        init_extraction = DataExtraction(text, data, model_name)
        response = init_extraction.map_extracted_properties()
        return Response(response, status=200, mimetype='application/json')

    @app.route('/v.0.1/getSimilarityMatrix', methods=['POST'])
    @auth.login_required
    def get_similarity():
        init_request = Request()
        texts = init_request.get_text_list()
        init_similarity = DocumentSimilarity(texts)
        response = init_similarity.calculate_document_similarity()
        return Response(response, status=200, mimetype='plain/text')

    return app


if __name__ == '__main__':
    app = flask_server()
    app.run()
