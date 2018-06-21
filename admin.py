# from prayer_bot.application import db,admin
from prayer_bot import db, admin
from .models import PrayerTeam,PrayerDB #, MyModelView
from flask_admin.contrib.sqla import ModelView





admin.add_view(ModelView(PrayerTeam,db.session))
admin.add_view(ModelView(PrayerDB,db.session))
