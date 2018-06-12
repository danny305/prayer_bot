from application import db
from sqlalchemy import exc
from pprint import pprint
import pandas as pd
from datetime import datetime
import pytz



#ToDo Figure out how to make the timestamp the right timezone.


class PrayerDB(db.Model):
    __tablename__ = 'prayer_db'
    id = db.Column('entry',db.INTEGER, primary_key=True, autoincrement=True)
    timestamp = db.Column('time_stamp',db.DATETIME(timezone=True),default=datetime.now(pytz.timezone('US/Central').replace(microsecond=0)))
    number = db.Column('phone_number', db.String(length=13),nullable=False)
    name = db.Column('name',db.String(25),nullable=True)
    prayer = db.Column('prayer',db.TEXT,nullable=False)
    private = db.Column('Private',db.BOOLEAN,default=True)
    __table_args__ = db.UniqueConstraint('phone_number','prayer',name='unique_prayer'),








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
    all_prayers = PrayerDB.query.all()
    headers = PrayerDB.__table__.columns.keys()
    rows = [[entry.id,entry.timestamp,entry.number,entry.name, entry.prayer] for entry in all_prayers]
    #pprint(headers)
    #pprint(rows)
    df = pd.DataFrame(data=rows,columns=headers).set_index('entry')
    print(df.to_string())
    return df



def create_excel(df=None):
    call_dt = datetime.now().strftime('%m-%d-%y_%H:%M')
    if df is None:
        df =create_prayer_df()
    writer = pd.ExcelWriter(path=f'prayer_{call_dt}.xlsx',engine='xlsxwriter')
    df.to_excel(writer)
    writer.save()
    print('Successfully created Excel File')




if __name__ == '__main__':
    #create_prayer_df()
    #create_excel()
    print(datetime.now().strftime('%m-%d-%y_%H:%M'))
    # update_from_excel('./prayer_05-28-18_21:33.xlsx')