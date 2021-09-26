import json
import pickle
from flask import Flask, render_template, request, make_response, jsonify
import pandas as pd

app = Flask(__name__)
# Load model
try:
    with open('bankrupt_model.pkl', 'rb') as file:
        bankrupt_model = pickle.load(file)
except:
    raise Exception("ERROR: *** Can find or Open Bankrupt Model! ***")

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    '''
    Call from UI via csv file upload
    '''
    csv_file = request.files['data']
    if not csv_file.filename.endswith('.csv'):
        return render_template(
            'index.html', error='Please choose file .csv only!')
    data_file = pd.read_csv(csv_file)
    predictions = bankrupt_model.predict(data_file)
    return render_template('index.html', predictions=predictions)

@app.route('/predict_bankrupt', methods=['POST'])
def predict_bankrupt():
    '''
    Predict via request API
    '''
    try:
        data = json.loads(request.data)
        data_predicts = data.get('data_predicts')
        predictions = bankrupt_model.predict(data_predicts)
        if predictions.tolist():
            response = make_response(
                jsonify({"predictions": predictions.tolist()}),
                200,
            )
    except Exception as e:
        response = make_response(jsonify({"error": e}), 400,)
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    app.run(port=3002, debug=True)
