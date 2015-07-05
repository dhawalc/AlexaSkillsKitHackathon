from django.db import models

class Intents(models.Model):
    intent = models.CharField(max_length=100)

    def __unicode__(self):
        return self.intent

class Slot(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
