from app import app
from flask import request, render_template, send_file
import gzip
import os
import io


@app.route('/login')
def login():
    author = '1149817'
    return author


@app.route('/zipper', methods=['GET', 'POST'])
def zipper():
    if request.method == 'POST':
        try:
            print(request.files)
            print(request.form)
            f_in = request.form.get('file')
            if isinstance(f_in, str):
                f_in = f_in.encode('utf-8')
            else:
                f_in = f_in.read()
            
            gzip_file = io.BytesIO(gzip.compress(f_in))
            
            return send_file(gzip_file, mimetype='application/gzip', download_name='result.gz')
        except Exception as e:
            return str(e)
        
    return render_template('form.html')

@app.route('/zipper2', methods=['GET', 'POST'])
def zipper2():
    if request.method == 'POST':
        try:
            print(request.files)
            print(request.form)
            f_in = request.form.get('file')
            if isinstance(f_in, str):
                f_in = f_in.encode('utf-8')
            else:
                f_in = f_in.read()
            
            gzip_file = io.BytesIO(gzip.compress(f_in))
            
            return send_file(gzip_file, mimetype='application/gzip', download_name='result.gz')
        except Exception as e:
            return str(e)
        
    return render_template('form2.html')
