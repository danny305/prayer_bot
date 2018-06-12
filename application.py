from flask import Flask, request, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from twilio.twiml import messaging_response

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prayer_data_table.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(application)
bs = Bootstrap(application)


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




if __name__ == '__main__':
    application.run(debug=True)
