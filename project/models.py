from flask import Flask, redirect, url_for
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    roles = db.relationship("Role", secondary="user_roles", back_populates="users")
    
    
    
class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
        
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))
        
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
        
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))