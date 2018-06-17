from prayer_bot.application import application,db,admin
from prayer_bot.prayer_sqlalchemy_db import PrayerTeam,PrayerDB, MyModelView





admin.add_view(MyModelView(PrayerTeam,db.session))
admin.add_view(MyModelView(PrayerDB,db.session))
