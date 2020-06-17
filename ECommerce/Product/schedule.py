from apscheduler.schedulers.background import BackgroundScheduler
from .scheduler_jobs import update_product_image_url
# from .models import Product


def scheduler_start():

    scheduler = BackgroundScheduler()
    scheduler.add_job(update_product_image_url, 'cron', hour=0)

    scheduler.start()
