# -*- coding: utf-8 -*-

from adaptor.model import CsvModel
from adaptor import fields


class MyCsvModel(CsvModel):
    year = fields.IntegerField()

    class Meta:
        delimiter = ","
