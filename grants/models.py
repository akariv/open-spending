# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
from geoposition.fields import GeopositionField
from djmoney.models.fields import MoneyField


class Regulation(models.Model):
    legacy_id = models.CharField(max_length=12)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = u'תקנה'
        verbose_name_plural = u'תקנות'
        ordering = ['name', ]

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
        ordering = ['name', ]

    def __unicode__(self):
        return self.name

    @classmethod
    def fill_from_csv_row(cls, row):
        try:
            organization = Organization.objects.get(name=row[u'שם הארגון'])
            organization.homepage = row[u'URL']
            organization.agenda = row[u'מטרות הארגון']
            organization.tags.add(row[u'תגיות'])
            organization.save()
        except Organization.DoesNotExist:
            pass


class Ministry(models.Model):
    legacy_id = models.IntegerField()
    name = models.CharField(u'שם המשרד', max_length=100)

    class Meta:
        verbose_name = u'משרד ממשלתי'
        verbose_name_plural = u'משרדים ממשלתיים'

    def __unicode__(self):
        return self.name


class GrantType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = u'סוג תמיכה'
        verbose_name_plural = u'סוגי תמיכות'

    def __unicode__(self):
        return self.name


class Grant(models.Model):
    year = models.PositiveIntegerField(u'שנה')
    target_organization = models.ForeignKey(Organization,
                                            verbose_name=u'עבור ארגון')
    related_number = models.IntegerField(u'מספר')
    budget_approved = MoneyField(u'תקציב שאושר', max_digits=10,
                                 decimal_places=2, default_currency='ILS')
    budget_transferred = MoneyField(u'תקציב שהועבר', max_digits=10,
                                    decimal_places=2, default_currency='ILS')
    regulation = models.ForeignKey('Regulation', verbose_name=u'תקנה')
    type = models.ForeignKey(GrantType, verbose_name=u'סוג התמיכה')
    ministry = models.ForeignKey('Ministry', verbose_name=u'משרד')

    def effective_budget(self):
        return '{percent:.2%}'.format(
            percent=self.budget_transferred / self.budget_approved)
    effective_budget.short_description = u'אחוז שנוצל'

    class Meta:
        verbose_name = u'העברת תקציב'
        verbose_name_plural = u'העברות תקציב'
        ordering = ['-budget_transferred']

    @classmethod
    def create_from_csv_row(cls, row):
        Grant.objects.create(
            year=row[u'שנה'],
            target_organization=Organization.objects.get_or_create(
                name=row[u'שם הארגון הנתמך'])[0],
            related_number=row[u'מספר התמיכות'],
            budget_approved=row[u'תקציב מאושר'],
            budget_transferred=row[u'תקציב שבוצע'],
            type=GrantType.objects.get_or_create(name=row[u'סוג התמיכה'])[0],
            regulation=Regulation.objects.get_or_create(
                name=row[u'שם התקנה'],
                legacy_id=row[u'קוד התקנה']
            )[0],
            ministry=Ministry.objects.get_or_create(name=row[u'שם המשרד'],
                                                    legacy_id=row['5800'])[0]
        )
