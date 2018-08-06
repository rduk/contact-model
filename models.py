from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from contact_model import db, ma

class Contact(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    fname = db.Column(db.String(100), nullable=False)
    sname = db.Column(db.String(100), nullable=False)

    def __init__(self, uname, email, fname, sname ):
        self.uname = uname
        self.email = email
        self.fname = fname
        self.sname = sname

    def __repr__(self):
        str = ("ID : {} ".format(self.id))
        str = ("User Name : {} ".format(self.uname))
        str += ("Email : {} ".format(self.email))
        str += ("First Name : {} ".format(self.fname))
        str += ("Surname : {} ".format(self.sname))
        return str


class MultiEmail(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)
    multi_emails = db.Column(db.String(1024), nullable=False)

    def __init__(self, contact_id, multi_emails):
        self.contact_id = contact_id
        self.multi_emails = multi_emails


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'uname', 'email', 'fname', 'sname')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


if __name__ == "__main__":
    db.create_all()
    print("End!!")