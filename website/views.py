
# views.py

from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app, send_from_directory, session, jsonify
import random
from flask_login import login_required, current_user
from sqlalchemy.sql import func  # Import the 'func' module
from .models import User
from . import db
from . import dtb
from . import vef_source




import os
from werkzeug.utils import secure_filename

views = Blueprint('views', __name__)


@views.route('/')
def index():
  return render_template("login.html")

@views.route('/handler')
@login_required
def home():
  return f"True"


@views.route('/<string:api_email>/<string:api_password>/<string:api_key>/handler')
def all(api_email, api_password, api_key):
  verify = vef_source.verify(api_email, api_password, api_key)
  if verify == False:
    return False
  else:
    User, Store, Product, Profile_View, View, Saved_Product, Team = dtb.get_all("User"), dtb.get_all("Store"), dtb.get_all("Product"), dtb.get_all("Profile_View"), dtb.get_all("View"), dtb.get_all("Saved_Product"), dtb.get_all("Team")
    return str([f"User: {User}, View: {View}, Product: {Product}, Profile_View: {Profile_View}, Store: {Store}"])



@views.route('/<string:api_email>/<string:api_password>/<string:api_key>/handler/get_all/<string:model>')
def get_all(api_email, api_password, api_key, model):
  verify = vef_source.verify(api_email, api_password, api_key)
  if verify == False:
    return False
  else: 
    return str(dtb.get_all(f"{model}"))

@views.route('/<string:api_email>/<string:api_password>/<string:api_key>/handler/find_all/<string:model>/<string:column>/<string:value>')
def find_all(api_email, api_password, api_key, model, column, value):
  verify = vef_source.verify(api_email, api_password, api_key)
  if verify == False:
    return False
  else: 
    return str(dtb.find_all(f"{model}", f"{column}", f"{value}"))

# @views.route('/<string:api_email>/<string:api_password>/<string:api_key>/handler/get_one/<string:key>')
# @login_required
# def get_one(api_email, api_password, api_key, key):
#   try:
#     return str(dtb.get_one(key))
#   except KeyError as e:
#     print(e)
#     return "None"

@views.route('/<string:api_email>/<string:api_password>/<string:api_key>/handler/add_one/<string:model>/<string:column>/<string:item>')

def add_one(api_email, api_password, api_key, model, column, item):
  verify = vef_source.verify(api_email, api_password, api_key)
  if verify == False:
    return False
  else:
    try:
      dtb.commit(dtb.add_one(model, column, item))
      # return f"Added {item} to column {column} in {model} Table"
      return "None"
    except Exception as e:
      print(e)
      return str(False) + str(e)

@views.route('/<string:api_email>/<string:api_password>/<string:api_key>/handler/add_entry/<string:model>/<string:column_value_pair>')
def add_entry(api_email, api_password, api_key, model, column_value_pair):
  verify = vef_source.verify(api_email, api_password, api_key)
  if verify == False:
    return False
  else:
    # try:
      # print(f"STR-->>>>{column_value_pair}\nLIST------>>>>> {eval(column_value_pair)}")
    dtb.commit(dtb.add_entry(model, column_value_pair))
    # return f"Added {item} to column {column} in {model} Table"
    return "None"
    # except Exception as e:
    #   print(f"Error-> {str(e)}\nCVP-> {column_value_pair}")
    #   return str(False) + str(e)
    
@views.route('/<string:api_email>/<string:api_password>/<string:api_key>/handler/find_one/<string:model>/<string:column>/<string:item>')

def find_one(api_email, api_password, api_key, model, column, item):
  verify = vef_source.verify(api_email, api_password, api_key)
  if verify == False:
    return False
  else:
    try:
      data = dtb.find_one(model, column, item)
      return f"{data}"
    except Exception as e:
      print(e)
      return f"Failed -> {e}"


@views.route('/<string:api_email>/<string:api_password>/<string:api_key>/handler/update_one/<string:model>/<string:column>/<string:item_search>/<string:item_update>')
def update_one(api_email, api_password, api_key, model, column, item_search, item_update):
  verify = vef_source.verify(api_email, api_password, api_key)
  if verify == False:
    return False
  else:
    try:
      item_id = dtb.find_one(model, column, item_search)
      if item_id == None:
        return f"Couldn't find `{column} -> {item_search}`"
      else:
        dtb.commit(dtb.update_one(model, item_id, column, item_update))
        # return f"Updated `{column} -> {item_search}` to `{column} -> {item_update}`"
        return "None"
      
    except Exception as e:
      return f"Update Failed -> {e}"

@views.route('/<string:api_email>/<string:api_password>/<string:api_key>/handler/update_entry/<string:model>/<string:column>/<string:column_value_pair>')
def update_entry(api_email, api_password, api_key, model, column, column_value_pair):
  verify = vef_source.verify(api_email, api_password, api_key)
  if verify == False:
    return False
  else:
    try:
      dtb.commit(dtb.update_entry(model, column, column_value_pair))
      return "None"
    except Exception as e:
      return f"Update Failed -> {e}"
  
@views.route('/<string:api_email>/<string:api_password>/<string:api_key>/handler/update_entry_dnd', methods=['POST'])
def update_entry_dnd(api_email, api_password, api_key):
  verify = vef_source.verify(api_email, api_password, api_key)
  if verify == False:
    return False
  else:
    try:
      dtb.commit(dtb.update_entry(request.form['model'], request.form['column'], request.form['cvp'], dnd=True))
      return "None"
    except Exception as e:
      return f"Update Failed -> {e}"

@views.route('/<string:api_email>/<string:api_password>/<string:api_key>/handler/delete_entry/<string:model>/<string:column>')
def delete_entry(api_email, api_password, api_key, model, column):
  verify = vef_source.verify(api_email, api_password, api_key)
  if verify == False:
    return False
  else:
    try:
      dtb.commit(dtb.delete_entry(model, column))
      return "None"
    except Exception as e:
      return f"Delete Failed -> {e}"



















