# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def RegVal(self, PostData):
        pass

    pass

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # create_at = datetime()
    # update_at = datetime()
    objects = UserManager()
