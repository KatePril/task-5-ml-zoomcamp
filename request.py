from requests import post

if __name__ == "__main__":
    url = "http://127.0.0.1:8080/predict"
    # client = {"job": "student", "duration": 280, "poutcome": "failure"}
    client = {"job": "management", "duration": 400, "poutcome": "success"}
    try:
        res = post(url, json=client)
        res.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        print(res.json())  # Print the JSON response
    except Exception as e:
        print(f"Error: {e}")