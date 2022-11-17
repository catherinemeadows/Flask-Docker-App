from flask import Flask, redirect
import requests
import random 
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def some_work():
    # decide if we'll send request to container B or container C
    list = [1,2]
    num = random.choice(list)

    # container B
    if num == 1:
        res = requests.post('http://localhost:18000/service_b')
        return "Finished container B call\n"
    
    # container C
    if num == 2:
        res = requests.post('http://localhost:18000/service_b')
        return "Finished container C call\n"


if __name__ == "__main__":
    app.run(debug=True)