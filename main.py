from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_request', methods=['POST'])
def send_request():
    url = 'https://api.sush.app/api/v1/pets/'+request.form['sushid']+'/feed'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODU4ODM4ODYsImlzcyI6InN1c2hpIiwiaWF0IjoxNjg1NzExMDg2LCJ1dWlkIjoiZjE2NWFmMDgtZWYyYS00NGU2LThhZDItYmU2NGUwYmNhZGU3In0.3jvAOs2_w-bs8IiiTfeTw5WLVrFRWLMxTUu9uA5t6Ew',
        'Content-Type': 'application/json',
    }
    data = {
        'quantity': request.form['corazones'],
        'is_free': False
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    return(str(response.status_code)+"<br><a href='/'>Index<a/>")

if __name__ == '__main__':
    app.run(debug=True)
