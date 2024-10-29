# Flask Essentials
from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app, send_from_directory, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

# Essential
import base64
import imghdr
import random
import json
from datetime import datetime, timedelta
import datetime as dt

# Utilites
from ..db import dbORM
from .. import encrypt
from .. import ScreenGoRoute
from .. import function_pool
import io # import subprocess
from .. import id_generator

# Artificial Intelligence Modules
# import openai
# from google.cloud import aiplatform
# from google.protobuf import json_format
# from google.protobuf.struct_pb2 import Value
from ..JaneAI import IntentActions
from ..JaneAI import DetectIntent

ArtificialIntelligenceEndpoints = Blueprint('ArtificialIntelligenceEndpoints', __name__)
aie = ArtificialIntelligenceEndpoints


@aie.route('/api/fspace-backend/ai/send-message', methods=['POST'])
def promptLLM():
    try:
        prompt = request.form['prompt']
        try:
            model = request.form['model']
        except:
            model = "base"
        jane = IntentActions.IntentActions(UserUniqueID=request.form['user_unique_id'], model=model) # initializes ai with the unser uniques id so the ai knows who it's dealing with
        response = jane.mapIntentToActions(DetectIntent.detect_intent(prompt), prompt)
            
        if isinstance(response, list):
            return jsonify({
                "message": {
                    "success": response[0],
                    "data": {
                        "type": f"{response[2]}s",
                        "trigger": f"{response[2]} search",
                        "links": response[3],
                        "ids": response[1]
                    }
                }
            })
        else:
            return function_pool.returnJSONData("success", response)
        # return function_pool.returnJSONData("success", {"prompt": prompt, "response": " ".join(response_list)})
    
    except Exception as e:
        return function_pool.returnJSONData("failed", f"Server Error: {e}")