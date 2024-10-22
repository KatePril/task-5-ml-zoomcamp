from requests import post

if __name__ == "__main__":
    url = "http://127.0.0.1:8080/predict"
    client = {"job": "student", "duration": 280, "poutcome": "failure"}
    res = post(url, json=client).json()
    print(res)