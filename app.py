from flask import Flask, request, render_template
import numpy as np
import os
import pickle
from werkzeug.utils import secure_filename

import cv2
import pytesseract

model = pickle.load(open('stock_senti.pkl', 'rb'))
tfvector=pickle.load(open('tfvector.pkl','rb'))

app=Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET', 'POST'])
def analyse():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'upload', secure_filename(f.filename))
        f.save(file_path)


        img=cv2.imread(file_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        data=pytesseract.image_to_string(img_rgb)
        #data=data.replace("[^a-zA-Z]", " ",regex=True, inplace=True)
        data=[data.lower()]
        data = tfvector.transform(data).toarray()
        pred=model.predict(data)
        result=['Stock will go down or remain same','Stock will go UP']

    return result[pred[0]]

if __name__=='__main__':
    app.run(debug=True)