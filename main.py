
from flask import Flask,request,jsonify
from model_files.ML import pipeline_transformer,num_pipeline_transformer,predict_mpg
import pickle


app= Flask('app')

@app.route('/', methods=['GET'])
def home():
    return 'Running in homepage!!'


@app.route('/test', methods=['GET'])
def test():
    return 'Running!!'

@app.route('/predict', methods=['POST'])
def predict():
    vehicle= request.get_json()
    print(type(vehicle))
    with open('./model_files/model.bin', 'rb') as f_in:
        SVR_model = pickle.load(f_in)
        f_in.close()
    predictions=predict_mpg(vehicle, SVR_model)
    result = {
        'mpg_prediction': list(predictions)
    }
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)    
