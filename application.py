from flask import Flask, request
application = Flask(__name__)

from twilio.twiml import messaging_response
if __name__ == '__main__':
    from prayer_sqlalchemy_db import insert_prayer







@application.route('/prayer',methods=['GET','POST'])
def prayer_text():
    resp = messaging_response.MessagingResponse()
    if request.method == 'POST':
        number = request.form['From']
        pray_request = request.form['Body']




if __name__ == '__main__':
    application.run(debug=True)
