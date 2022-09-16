from apscheduler.schedulers.background import BackgroundScheduler
from web.views import EventViewSet




def start():
    scheduler = BackgroundScheduler()
    reminder = EventViewSet()
    scheduler.add_job(reminder._get_upcomings, "interval", minutes = 1, id="reminder_001", replace_existing=True)
    scheduler.start()