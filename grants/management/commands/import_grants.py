from django.core.management.base import BaseCommand
from grants.csv_models import MyCsvModel
import codecs


class Command(BaseCommand):

    def handle(self, *args, **options):

        my_csv_list = MyCsvModel.import_data(
            data=codecs.open('data/grants.csv', encoding='utf-8'))
