from flask import Flask, render_template, request
from rfc_predictor import predict_flower_class

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predict')
def predict_form():
    return render_template('predict.html')

@app.route('/thankyou')
def thank_you():
    sl = float(request.args.get("sepal_length"))
    sw = float(request.args.get("sepal_width"))
    pl = float(request.args.get("petal_length"))
    pw = float(request.args.get("petal_width"))
    prediction = predict_flower_class(sl,sw,pl,pw)
    return render_template('thankyou.html' , prediction=prediction.capitalize())

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_tem

if __name__ == '__main__':
    app.run(debug=True)
