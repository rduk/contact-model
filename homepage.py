from flask import Blueprint, render_template, make_response
from flask_restful import Api, Resource

app_hp_bp = Blueprint('homepage', __name__, template_folder='templates/homepage')
api_hp = Api(app_hp_bp)


class Homepage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html', api_hp=api_hp), 200, headers)

    def post(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html', api_hp=api_hp), 200, headers)


class CreateContact(Resource):
    def post(self):
        headers = {'Content-Type': 'Text/html'}
        return make_response(render_template('/v1/create_contact.html'), 200, headers)


api_hp.add_resource(Homepage, '/', endpoint='homepage')
api_hp.add_resource(CreateContact, '/create_contact_v1', endpoint='createcontact')


