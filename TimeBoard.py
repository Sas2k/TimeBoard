#Author Sasen Perera
#started on 2021.09.10 end on 2021/09/25 [Hackathon Time Period]
#after hackathon dev time - yyyy/mm/dd - last updated after hackathon
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
#from flask_ngrok import run_with_ngrok
import requests

# from flask_mail import*
# from datetime import timedelta
app = Flask(__name__)
# mail = Mail(app)
app.secret_key = 'qwertyuioplkjhgfdsazxcvbnm1029384756'
# app_permanent_session_lifetime = timedelta(days = 1)
#!While using the web do not turn off the server and on it will cause to crash the web pages and the info!#
#TODO|1|Fix Name Error
#*done|2|Style Website
#TODO|3|Make a time detection system
#*done|4|Figure out the SMS A.P.I.
#!Not Possible for now|5|Make a timecard system so the second time card doesn't reset
@app.route('/index.html')
def Main():
   return render_template('index.html')
@app.route('/Calender.html', methods=["POST", "GET"])
def Calender():
   if request.method == 'POST':
      global name
      global Time
      global date
      name = request.form.get('Name')
      Time = request.form.get('time')
      date = request.form.get('date')

      session["name"] = name
      session["Time"] = Time
      session["date"] = date

      print('name:')
      print(name)
      print('time:')
      print(Time)
      print('date:')
      print(date)
      return render_template('Calender.html', name = name, Time = Time, date = date)
   if 'name' in session:
      return render_template('Calender.html', name = name, Time = Time, date = date)
   else:
      return render_template('Calender.html')
@app.route('/About.html')
def about():
   return render_template('About.html')

@app.route('/New_Event.html', methods=["GET", "POST"])
def new_event():
   return render_template('New_Event.html')
def submit():
   url = "http://localhost:5678/sms/send"

   payload = "{\r\n\"version\": \"1.0\",\r\n\"applicationId\": \"APP_062045\",\r\n\"password\": \"c81529eb84b29dfb5a32af3978c5c6ef\",\r\n\"message\": \"Hello you have made an event on TimeBoard\",\r\n\"destinationAddresses\": [\r\n\"tel:94740050462\"\r\n],\r\n\"sourceAddress\": \"77000\",\r\n\"deliveryStatusRequest\": \"1\",\r\n\"encoding\": \"245\",\r\n\"binaryHeader\": \"526574697265206170706c69636174696f6e20616e642072656c6561736520524b7320696620666f756e642065787069726564\"\r\n}"
   headers = {
   'msg': 'hello '
   }

   response = requests.request("POST", url, headers=headers, data=payload)

   print(response.text)
   print('sms sent')
   return redirect('Calender.html')

@app.route('/sms/recive', methods=['POST', 'GET'])
def sms_recive():
   print('??')

@app.route('/sms/send', methods=['POST'])
def sms_send():
   print('!!')

if __name__ == '__main__':
   print('Started')
   app.run('127.0.0.1', '5678', False)
   #run_with_ngrok(app)
   print('End')
