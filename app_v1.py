from flask import redirect, request, make_response, Blueprint, url_for
from json import dumps
from flask_restful import Api, Resource, abort
from contact_model import models, db

app_v1_bp = Blueprint('app_v1', __name__, template_folder='templates/v1')
api_v1 = Api(app_v1_bp)

def jsonify_api(status=400, indent=4, **kwargs):
    response = make_response(dumps(kwargs, indent=indent))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.stutus_code = status
    return response


class ContactModelAll(Resource):
    def post(self):
        uname = request.args.get('uname') if request.args.get('uname') else request.form.get('uname')
        email = request.args.get('email') if request.args.get('email') else request.form.get('email')
        fname = request.args.get('fname') if request.args.get('fname') else request.form.get('fname')
        sname = request.args.get('sname') if request.args.get('sname') else request.form.get('sname')
        contact = models.Contact(uname, email, fname, sname)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('homepage.homepage'))

    def get(self):
        contacts = models.Contact.query.all()
        result = models.users_schema.dump(contacts)
        all_contacts = {'contacts': result.data}
        return jsonify_api(**all_contacts)


class ContactModelUname(Resource):
    def get(self, uname):
        user = models.Contact.query.filter_by(uname=uname).first()
        if not user:
            abort(404)
        result = models.user_schema.dump(user)
        res_uname = {'user': result.data}
        return jsonify_api(**res_uname)

    def delete(self, uname):
        user = models.Contact.query.filter_by(uname=uname).first()
        db.session.delete(user)
        db.session.commit()
        return models.user_schema.jsonify(user)

    def put(self, uname):
        user = models.Contact.query.filter_by(uname=uname).first()
        email = request.args.get('email') if request.args.get('email') else request.form.get('email')
        fname = request.args.get('fname') if request.args.get('fname') else request.form.get('fname')
        sname = request.args.get('sname') if request.args.get('sname') else request.form.get('sname')
        user.email = email
        user.fname = fname
        user.sname = sname
        db.session.commit()
        return models.user_schema.jsonify(user)


api_v1.add_resource(ContactModelAll, '/allcontacts')
api_v1.add_resource(ContactModelUname, '/allcontacts/<string:uname>')
