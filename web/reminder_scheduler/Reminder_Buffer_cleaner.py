from apscheduler.schedulers.background import BackgroundScheduler
from web.views import ReminderAPI



def start():
    scheduler = BackgroundScheduler()
    Buffer = ReminderAPI()
    scheduler.add_job(Buffer._clear, "interval", minutes = 10, id="Buffer_Cleaner_001", replace_existing=True)
    scheduler.start()