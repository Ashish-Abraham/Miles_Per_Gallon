import requests
url = "http://localhost:9696/predict"

vehicle_config = {
    'Cylinders': [4,6,6],
    'Displacement': [155.0,144.2,144.2],
    'Horsepower': [93.0,100.0,93.0],
    'Weight': [2500.0,1900.0,1900.0],
    'Acceleration': [15.0,12.0,13.0],
    'Model Year': [81,82,80],
    'Origin': [3,2,1],
    'displacement_on_power': [1.234,1.234,1.234],
    'weight_on_cylinder': [530.00,523.00,520.00],
    'acceleration_on_power': [0.25,0.21,0.23],
    'acceleration_on_cyl': [4.21,3.24,4.01],
}

r = requests.post(url, json = vehicle_config)
print(r.text.strip())