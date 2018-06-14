from flask import Flask, request, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from twilio.twiml import messaging_response
from datetime import datetime
from prayer_tools import find_most_recent_excel
from os.path import abspath
from glob import glob


application = Flask(__name__)
application.config.from_pyfile('prayerconfig.cfg')



db = SQLAlchemy(application)
bs = Bootstrap(application)
mail = Mail(application)


if __name__ == '__main__':
    from prayer_sqlalchemy_db import insert_prayer

@application.route('/')
@application.route('/home')
def index():
    content = {'header': 'Welcome to the 2nd Baptist Prayer Bot'}
    return render_template('index.html', content = content)


@application.errorhandler(404)
def page_not_found(e):
    content = {'href': 'index','header': 'Prayer Bot Homepage'}
    return render_template('404.html',content = content), 404


@application.route('/prayer',methods=['GET','POST'])
def prayer_text():
    resp = messaging_response.MessagingResponse()
    if request.method == 'POST':
        number = request.form['From']
        pray_request = request.form['Body']

@application.route('/send_excel_email/<filename>')
@application.route('/send_excel_email/')
def send_excel(filename=None, attach=None):
    time = datetime.now().strftime('%m/%d %H:%M')
    email = Message(f'Prayer Bot Email {time}',
                  #sender='danny.jesus.diaz.94@gmail.com',
                  recipients=['danny.jesus.diaz.94@gmail.com','maritzaashtonsirven@gmail.com'])

    if filename is None:
        #file_path = abspath(find_most_recent_excel())
        file_path = glob('*.csv')[0]
        print(file_path)
        email.attach(file_path,content_type='text/csv')
        #email.attach(bytes(file_path,encoding='UTF-8'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    else:
        email.body = 'A filename was passed to the url.'

    mail.send(email)
    print('The email has been sent')
    return 'email sent!'

if __name__ == '__main__':
    application.run(debug=True)
