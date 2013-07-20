# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import unicodecsv
from grants import models


class Command(BaseCommand):

    def handle(self, *args, **options):
        for row in unicodecsv.DictReader(open('data/grants.csv')):
            models.Grant.create_from_csv_row(row)
        for row in unicodecsv.DictReader(open('data/organizations.csv')):
            models.Organization.fill_from_csv_row(row)
