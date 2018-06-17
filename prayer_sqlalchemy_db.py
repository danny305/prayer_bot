from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from prayer_bot.application import db

from enum import Enum
from sqlalchemy import exc

#from sqlalchemy_utils.types.choice import ChoiceType   #This is another way to do Enum but it does not show up on the flask admin page so I am trying to do Enum


from pprint import pprint
import pandas as pd
from datetime import datetime,timedelta
import pytz



#ToDo Figure out how to make the timestamp the right timezone.


class PrayerDB(db.Model):
    __tablename__ = 'prayer_db'
    id = db.Column('id',db.INTEGER, primary_key=True, autoincrement=True)
    timestamp = db.Column('timestamp',db.DATETIME,default=db.func.now())
    phone_number = db.Column('phone_number', db.String(length=13),nullable=False)
    name = db.Column('name',db.String(25),nullable=True)
    prayer = db.Column('prayer',db.TEXT,nullable=False)
    private = db.Column('private',db.BOOLEAN,default=True)
    __table_args__ = db.UniqueConstraint('phone_number','prayer',name='unique_prayer'),


class Groups(Enum):
    SURFACE = '18-21'
    MVMT = '22-25'
    LOFT = '26-29'
    NA = 'N/A'



class PrayerTeam(db.Model,UserMixin):
    __tablename__ = 'prayer_team'

    id = db.Column('id', db.INTEGER, primary_key=True)
    name = db.Column('name', db.String(length=40), nullable=False)
    phone_number = db.Column('phone_number', db.String(length=15), nullable=False)
    email = db.Column('email', db.String(length=50), nullable=False)
    group = db.Column('group', db.Enum(Groups), nullable=False)



#table for User accounts to login
class Users(db.Model,UserMixin):
    __tablename__ = 'users_db'
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(length=40), nullable=False)
    password = db.Column(db.String(length=25), nullable=False)
    __table_args__ = db.UniqueConstraint('username','password'),




#Create your own ModelView class where you override the is_accessible method in order to not allow the admin page to be accessible to everyone.
class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated












def insert_prayer(number=None,prayer=None,name=None):
    request = PrayerDB(number=number,prayer=prayer, name=name)
    try:
        db.session.add(request)
        db.session.commit()

    except exc.IntegrityError:
        db.session.rollback()
        print('This entry already has been entered to the prayer database.')
        return ValueError


#ToDo learn how to update a db from the cells in a excel file.
def update_from_excel(excel_file):
    """This function is to update the DB name column from names manually inserted into the excel file"""
    excel_handle = pd.read_excel(excel_file)
    print(excel_handle.to_string())
    print('Successfully imported excel file into a DataFrame.')






#ToDo Write a function to take the imported excel file DF and compare it to the current DF generated and do an Outer Join. I can use this to find the new prayers added in the last day.
def outer_join_df(imp_df=None):
    pass







def create_prayer_df():
    headers = PrayerDB.__table__.columns.keys()
    rows = [[getattr(row,col) for col in headers] for row in PrayerDB.query.all()]
    #pprint(headers)
    #pprint(rows)
    df = pd.DataFrame(data=rows,columns=headers).set_index('id')
    print(df.to_string())
    return df



def create_excel(df=None):
    call_dt = datetime.now().strftime('%m-%d-%y_%H:%M')
    if df is None:
        df =create_prayer_df()
    writer = pd.ExcelWriter(path=f'../prayers_{call_dt}.xlsx',engine='xlsxwriter')
    df.to_excel(writer)
    writer.save()
    print('Successfully created Excel File')


def create_csv(df=None):
    call_dt = datetime.now().strftime('%m-%d-%y_%H:%M')
    if df is None:
        df = create_prayer_df()
    df.to_csv(path_or_buf=f'../prayers_{call_dt}.csv',)
    print('Successfully made the csv')



if __name__ == '__main__':
    #create_prayer_df()
    #create_excel()
    print(datetime.now().strftime('%m-%d-%y_%H:%M'))
    # update_from_excel('./prayer_05-28-18_21:33.xlsx')
    #create_csv()
    db.create_all()
