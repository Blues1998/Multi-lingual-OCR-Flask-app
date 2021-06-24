from flask import Flask, render_template, url_for, request, redirect
import os
from PIL import Image
import pytesseract
import pdf2image

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def pdf_to_image(pdf):
    pil_images = pdf2image.convert_from_path(pdf, 500, grayscale=True)
    return pil_images


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("upload.html")


@app.route('/upload', methods=["POST"])
def upload():
    result = 0
    target = os.path.join(APP_ROOT, 'static/images')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        if upload.filename == '':
            result = 1
        else:
            print(upload)
            # Check if file is in pdf format
            is_pdf = upload.filename[-3:] == 'pdf'
            if is_pdf:
                upload = pdf_to_image(upload)
            print("{} is the file name".format(upload.filename))
            filename = upload.filename
            destination = "/".join([target, "temp.jpg"])
            # destination = destination.replace("/", "")
            print("Accept incoming file: ", filename)
            print("Save it to: ", destination)
            upload.save(destination)
    # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    if result == 0:
        result = pytesseract.image_to_string(Image.open(destination), lang='eng+tel+urd+hin')
        print("Destination: ", destination)
        print(result)
    else:
        result = "No image uploaded"
    return render_template("upload.html", result=result)
    # return render_template("complete.html", result=result)


@app.route('/about', methods=["GET", "POST"])
def about():
    render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
