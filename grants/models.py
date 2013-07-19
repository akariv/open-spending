# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
from geoposition.fields import GeopositionField


class Grant(models.Model):
    GRANT_TYPES = [
        (1, u'תשלומי תמיכה נוספים'),
        (2, u'תמיכה ברשויות מקומיות'),
        (3, u'הקצבות'),
        (4, u"תמיכה במוסדות ציבור (3א')"),
        (5, u'מענקי איזון'),
        (6, u'תמיכה כלכלית'),
        (7, u'תמיכה בפרט'),
        (7, u'תמיכות אחרות'),
    ]

    year = models.PositiveIntegerField(u'שנה')
    target_organization = models.ForeignKey('Organization',
                                            verbose_name=u'עבור ארגון')
    reason = models.TextField(u'סיבה')
    related_number = models.IntegerField(u'מספר')
    budget_approved = models.IntegerField(u'תקציב שאושר')
    budget_transferred = models.IntegerField(u'תקציב שהועבר')
    regulation = models.ForeignKey('Regulation', verbose_name=u'תקנה')
    type = models.IntegerField(u'סוג התמיכה', choices=GRANT_TYPES)
    ministry = models.ForeignKey('Ministry')

    class Meta:
        verbose_name = u'תמיכה'
        verbose_name_plural = u'תמיכות'

    def __unicode__(self):
        return self.target_organization


class Regulation(models.Model):
    legacy_id = models.CharField(max_length=12)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = u'תקנה'
        verbose_name_plural = u'תקנות'

    def __unicode__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(u'שם הארגון', max_length=100)
    tags = TaggableManager()
    homepage = models.URLField(u'אתר בית')
    agenda = models.TextField(u'מטרות הארגון')
    position = GeopositionField()

    class Meta:
        verbose_name = u'ארגון'
        verbose_name_plural = u'ארגונים'

    def __unicode__(self):
        return self.name


class Ministry(models.Model):
    legacy_id = models.IntegerField()
    name = models.CharField(u'שם המשרד', max_length=100)

    class Meta:
        verbose_name = u'משרד ממשלתי'
        verbose_name_plural = u'משרדים ממשלתיים'

    def __unicode__(self):
        return self.name
