# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route('/')
# def student():
#    return render_template('student.html')

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)

# if __name__ == '__main__':
#    app.run(debug = True)
import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
from glob import glob

app = Flask(__name__)

UPLOAD_FOLDER = 'pics/'
ALLOWED_EXTENSIONS = set(['png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_name():
   return render_template('face_scan.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        user = request.form.get("user")
        if file:
            filename = secure_filename(file.filename)
            pics = glob(os.path.join(app.config['UPLOAD_FOLDER'], user + "_*.png"))
            last_pic = sorted(pics)[-1]
            _, numb = last_pic.split("_")
            numb = int(numb) + 1
            filenmae = f"{user}_numb.png"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'Success'
    return "Failed"

if __name__ == '__main__':
   app.run(debug = True)