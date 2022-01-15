
from flask import Flask,request,jsonify
from model_files.model import predict_mpg
import pickle

app= Flask('app')

@app.route('/test', methods=['GET'])
def test():
    return 'Running!!'

@app.route('/predict', methods=['POST'])
def predict():
    vehicle= request.get_json()
    print(vehicle)
    SVR_model= pickle.load('./model_files/MPG_SVR.pkl')
    predictions=predict_mpg(vehicle, SVR_model)
    result = {
        'mpg_prediction': list(predictions)
    }
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)    
