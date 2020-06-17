from django.apps import AppConfig
from . import schedule


class ProductConfig(AppConfig):
    name = 'Product'

    def ready(self):
        schedule.scheduler_start()
