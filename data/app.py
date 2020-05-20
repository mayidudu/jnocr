from flask import Flask, render_template,request
import os
from PIL import Image
import pytesseract

app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
@app.route("/")
def hello_world():
    result_text = "xxxxxx"
    return render_template('index.html',result = result_text)

@app.route("/up_photo",methods=['POST'])
def up_photo():
    img = request.files.get('txt_photo')
    path = basedir
    file_path=path+"/"+ img.filename
    img.save(file_path)
    text=pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')
    print(file_path)
    print("in up photo")
    return "success:" + text

@app.route("/upphoto",methods=['post'])
def upphoto():
    img = request.files.get('txt_photo')
    path = basedir
    file_path=path + "/"+img.filename
    img.save(file_path)
    text=pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')
    return render_template('index.html',result=text)

if __name__ == '__main__':
    app.run(debug=True)

