# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class LinkSaver(models.Model):    
    title = models.CharField(max_length=100)
    href = models.URLField(max_length=200) 


    
    

    

