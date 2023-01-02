from flask import Flask, render_template, request
from app import app
import numpy as np
import pickle
app = Flask(__name__)
needColumn=pickle.load(open("ModelCreation/needColumn.pkl","rb"))
pipeline=pickle.load(open("ModelCreation/pipeline.pkl","rb"))


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route("/output", methods=['POST', 'GET'])
@app.route("/output")
def predict():
    if request.method != 'POST':
        return render_template("error.html")
    all_column=needColumn.copy()
    all_column.insert(15,"veil-type")
    Gotvalues = [request.form[col] for col in all_column]
    Gotvalues.pop(15)
    val=pipeline.predict(np.array(Gotvalues).reshape(1,-1))
    result="Something Wrong!"
    if val[0]=='e':
        result="This mushroom is edible"
    else:
        result="This mushroom is poison"

    return  render_template('output.html',r=result)

if __name__ == "__main__":
    app.run(debug=True)
