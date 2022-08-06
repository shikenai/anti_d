from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class DisasterName(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class LocalGovernment(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    phone_number_regex = RegexValidator(regex=r'^[0-9]+$',
                                        message='Tel Number must be entered in the format: "09012345678". Up to 15 digits allowed.')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=15, verbose_name='電話番号')

    def __str__(self):
        return self.name


class OrganizationType(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    models.ForeignKey(LocalGovernment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RelatedOrganization(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Report(models.Model):
    report_title = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField('作成日時', blank=True, null=True)
    hearing_at = models.DateTimeField('ヒアリング日時', blank=True, null=True)
    related_organization = models.ForeignKey(to=RelatedOrganization, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    disaster_name = models.ForeignKey(to=DisasterName, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '【' + self.disaster_name.name + '】' + self.related_organization.name + ' ' + str(self.hearing_at)
