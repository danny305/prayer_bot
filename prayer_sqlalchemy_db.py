from flask_sqlalchemy import SQLAlchemy
from application import application
from sqlalchemy import exc

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prayer_data_table.db'
application.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(application)




class PrayerDB(db.Model):
    __tablename__ = 'prayer_db'
    id = db.Column('entry',db.INTEGER, primary_key=True, autoincrement=True)
    timestamp = db.Column('time_stamp',db.DATETIME(timezone=True),default=db.func.now())
    number = db.Column('phone_number', db.String(length=13),nullable=False)
    name = db.Column('name',db.String(25),nullable=True)
    prayer = db.Column('prayer',db.TEXT,nullable=False)
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
    pass