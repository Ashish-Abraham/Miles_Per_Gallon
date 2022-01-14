
from flask import Flask

app= Flask('app')

@app.route('/test', methods=['GET'])
def test():
    return 'First one!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)    