from django.db import models

# Create your models here.

class InsertTmbh(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)
    number1 = models.IntegerField(blank=True, null=True)
    number2 = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    def publish(self):
            self.published_date = timezone.now()
            self.save()
    def __unicode__(self):
        return u"%s" % self.name