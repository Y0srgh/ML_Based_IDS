import requests

# Define the API endpoint
url = "http://localhost:8000/predict/"

# Example data from the dataset
sample_data_0 = [
    445, 6, 100000, 2, 2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 5.819214464239472, 100000.0, 100000.0, 100000.0, 20.0, 100000.0,
    100000.0, 0.0, 100000.0, 100000.0, 100000.0, 100000.0, 0.0, 100000.0,
    100000.0, 0, 0, 0, 0, 64, 40, 2.909607232119736, 2.909607232119736, 0.0,
    0.0, 0.0, 0.0, 0.0, 0, 0, 0, 1, 0, 0, 0, 0, 1.0, 0.0, 0.0, 0.0, 0, 0, 0,
    0, 0, 0, 2, 0, 2, 0, 8192, 0, 0, 32, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 57958.0
]

sample_data_01 = [
    3389,6,100000,15,9,1460.0,1731.0,741.0,0.0,97.33333333333331,189.91263655641643,
    1179.0,0.0,192.3333333333333,386.0744746807279,481.7253830177234,3.623130426958747,
    100000.0,100000.0,100000.0,35.0,100000.0,100000.0,100000.0,100000.0,100000.0,100000.0,
    100000.0,100000.0,100000.0,100000.0,0,0,0,0,312,192,2.264456516849217,1.3586739101095302,
    0.0,1179.0,127.64000000000004,271.1933320222556,73545.82333333335,0,0,1,1,0,0,0,1,0.0,
    132.95833333333334,97.33333333333331,192.3333333333333,0,0,0,0,0,0,15,1460,9,1731,8192,64000,
    7,20,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4122.0
]

sample_data_02 = [
    80,6,57,2,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,35087.71929824561,57.0,0.0,57.0,57.0,57.0,
    57.0,0.0,57.0,57.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,40,0,35087.71929824561,0.0,0.0,0.0,0.0,0.0,0.0,0,0,
    0,0,1,0,0,0,0.0,0.0,0.0,0.0,0,0,0,0,0,0,2,0,0,0,2238,-1,0,20,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,50297.0
]

sample_data_1 = [
    80,6,100000,2,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.110934208,100000.0,0.0,100000.0,100000.0,
    100000.0,100000.0,0.0,100000.0,100000.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,40,0,0.110934208,0.0,0.0,0.0,0.0,0.0,
    0.0,0,0,0,0,1,0,0,0,0.0,0.0,0.0,0.0,0,0,0,0,0,0,2,0,0,0,2049,-1,0,20,0.0,0.0,0.0,0.0,100000.0,0.0,100000.0,
    100000.0,62070.0
]

sample_data_11 = [
    80,6,100000,2,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.170796454,100000.0,0.0,100000.0,
    100000.0,100000.0,100000.0,0.0,100000.0,100000.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,40,0,0.170796454,
    0.0,0.0,0.0,0.0,0.0,0.0,0,0,0,0,1,0,0,0,0.0,0.0,0.0,0.0,0,0,0,0,0,0,2,0,0,0,2049,-1,0,20,0.0,
    0.0,0.0,0.0,100000.0,0.0,100000.0,100000.0,49784.0
]

# Format the payload
payload = {"data": sample_data_11}

# Make the POST request
response = requests.post(url, json=payload)

# Print the response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Failed to get a prediction: {response.status_code}, {response.text}")