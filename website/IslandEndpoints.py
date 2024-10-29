# Flask Essentials
from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app, send_from_directory, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

# Essential
import base64
import imghdr
import ast
import random
from datetime import datetime, timedelta
import datetime as dt

# Utilites
from . import encrypt
# from . import function_pool
from . import id_generator


IslandEndpoints = Blueprint('IslandEndpoints', __name__)
ise = IslandEndpoints

@ise.route("/payments/render-payment-page/<string:first_name_encrypted>/<string:last_name_encrypted>/<string:email_encrypted>/<string:amount_encrypted>/<string:product_id_encrypted>")
def renderPaymentPage(first_name_encrypted, last_name_encrypted, email_encrypted, amount_encrypted, product_id_encrypted):
    
    return render_template("PaymentScreen.html",
        first_name = encrypt.decrypter(first_name_encrypted),
        last_name = encrypt.decrypter(last_name_encrypted),
        email = encrypt.decrypter(email_encrypted),
        amount = encrypt.decrypter(amount_encrypted),
        apiKey = encrypt.decrypter(encrypt.decrypter("&amp;&&1;&&2;&sm;&amp;&&1;&&0;&sm;&amp;&021;&014;&004;&sm;&amp;&&1;&&9;&sm;&amp;&&0;&&4;&sm;&amp;&&1;&&8;&sm;&amp;&&1;&&9;&sm;&amp;&021;&014;&004;&sm;&amp;&&0;&&3;&sm;&amp;&&0;&&1;&sm;&amp;&&1;&&6;&sm;&amp;&&1;&&6;&sm;&amp;&&0;&&5;&sm;&amp;&amp;&&0;&sm;&amp;&&0;&&0;&sm;&amp;&amp;&&5;&sm;&amp;&&1;&&5;&sm;&amp;&amp;&&5;&sm;")),
        contractCode = encrypt.decrypter(encrypt.decrypter("&amp;&amp;&&7;&sm;&amp;&amp;&&2;&sm;&amp;&amp;&&0;&sm;&amp;&amp;&&8;&sm;&amp;&amp;&&4;&sm;&amp;&amp;&&5;&sm;&amp;&amp;&&0;&sm;&amp;&amp;&&3;&sm;&amp;&amp;&&5;&sm;&amp;&amp;&&6;&sm;")),
        product_id = product_id_encrypted,
        description = f"Payment for Product by {encrypt.decrypter(email_encrypted)} with Monnify."
        )