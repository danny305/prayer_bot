from flask import request, render_template, url_for, redirect, session
from flask_mail import Message
from flask_login import login_user, logout_user, login_required, current_user
from twilio.twiml import messaging_response

from prayer_bot.application import application, db, mail, login_manager
from prayer_bot.prayer_tools import find_most_recent
from prayer_bot.prayer_sqlalchemy_db import Users
from prayer_bot.prayer_forms import LoginForm
import prayer_bot.prayer_admin

from datetime import datetime
from os.path import abspath

login_manager.login_view = 'form'
login_manager.login_message = 'You need to login before you proceed.'


@application.route('/')
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
        file_path = abspath(find_most_recent(query='*.csv',create=True))
        with application.open_resource(file_path) as fp:
            email.attach(file_path,content_type='text/csv',data=fp.read())
            #email.attach(file_path, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                        # data=fp.read())
    else:
        email.body = 'A filename was passed to the url.'

    mail.send(email)
    print('The email has been sent')
    return 'email sent!'



@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


"""Login Homepage"""
@application.route('/login',methods=['GET','POST'])
def form():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data,password=form.password.data).first()
        if user:
            login_user(user)

            if 'next' in session:
                next = session['next']
                return redirect(next,code=302)

            return redirect('/', code=302)
        else:
            return '<h1>User not found</h1>'
    return render_template('form.html',form=form)




"""Protected Page"""
@application.route('/home')
@login_required
def home():
    return f"Welcome big boss."


"""Logout Page"""
@application.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are have been logged out.'


if __name__ == '__main__':
    application.run(debug=True)