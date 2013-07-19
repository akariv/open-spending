# -*- coding: utf-8 -*-
from django.db import models
from easy_maps.models import Address


class Grant(models.Model):
    year = models.PositiveIntegerField(u'שנה')

    class Meta:
        verbose_name = u'תמיכה'
        verbose_name_plural = u'תמיכות'

    def __unicode__(self):
        pass


class Organization(models.Model):
    name = models.CharField(u'שם הארגון', max_length=100)
    homepage = models.URLField(u'אתר בית')
    agenda = models.TextField(u'מטרות הארגון')
    address = Address()

    class Meta:
        verbose_name = u'ארגון'
        verbose_name_plural = u'ארגונים'

    def __unicode__(self):
        pass
