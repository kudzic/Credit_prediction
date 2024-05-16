from flask import Flask,render_template,request
import numpy as np
import pickle
app = Flask(__name__)

model=pickle.load(open('predict.pkl','rb'))
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    print(int_features)
    final=[np.array(int_features)]
    prediction=model.predict(final)
    print(prediction)

    if(prediction[0]==0) :
         return render_template("index.html",pred="You have bad credit")

    if (prediction[0] == 1):
        return render_template("index.html", pred="You have standard credit")
    if (prediction[0] == 2):
        return render_template("index.html", pred="You have good credit")
    return "Predicted this"


if __name__ == '__main__':
    app.run()
