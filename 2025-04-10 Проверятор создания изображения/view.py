from app import app
from flask import request, Response
import os
import io
from PIL import Image


img_name = 'smirk.png'


@app.route('/login')
def login():
    author = '1149817'
    return author


@app.route('/makeimage')
def makeimage():
    if request.args:
        width = int(request.args.get('width'))
        height = int(request.args.get('height'))
        
        img_path = os.path.join(app.config['IMG_FOLDER'], img_name)

        with Image.open(img_path) as img:

            new_img = img.resize((width, height))

            b  = io.BytesIO()

            new_img.save(b, format='png')
            img_bytes = b.getvalue()

            return Response(img_bytes, mimetype='image/png')
    
    return "Please provide width and height in following format: <path_way>?width=100&height=200"
