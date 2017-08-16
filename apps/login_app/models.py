# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def RegVal(self, PostData):
        results = {"status": True, 'errors': [] }
        if len(PostData['first_name']) < 2:
            results['errors'].append("first name must be 3 or more characters")
        if len(PostData['last_name']) < 2:
            results['errors'].append("last name must be 3 or more characters")
        if re.(PostData['email']) :
            results['errors'].append("first name must be 3 or more characters")
        return results;

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # create_at = datetime()
    # update_at = datetime()
    objects = UserManager()
