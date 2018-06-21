# from prayer_bot.application import db,admin
from prayer_bot import db, admin
from .models import PrayerTeam,PrayerDB, MyModelView





admin.add_view(MyModelView(PrayerTeam,db.session))
admin.add_view(MyModelView(PrayerDB,db.session))
