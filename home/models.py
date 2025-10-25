# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Yearsession(models.Model):

    #__Yearsession_FIELDS__
    yrsession = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Yearsession_FIELDS__END

    class Meta:
        verbose_name        = _("Yearsession")
        verbose_name_plural = _("Yearsession")


class Instituteclasses(models.Model):

    #__Instituteclasses_FIELDS__
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Instituteclasses_FIELDS__END

    class Meta:
        verbose_name        = _("Instituteclasses")
        verbose_name_plural = _("Instituteclasses")


class Sections(models.Model):

    #__Sections_FIELDS__
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Sections_FIELDS__END

    class Meta:
        verbose_name        = _("Sections")
        verbose_name_plural = _("Sections")


class Departments(models.Model):

    #__Departments_FIELDS__
    shortname = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(blank=True, null=True, default=timezone.now)
    update_on = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Departments_FIELDS__END

    class Meta:
        verbose_name        = _("Departments")
        verbose_name_plural = _("Departments")



#__MODELS__END
