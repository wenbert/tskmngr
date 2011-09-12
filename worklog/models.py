from django.db import models

# Create your models here.

class Worklog(models.Model):
    title = models.CharField(max_length=200)
    desc  = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now=True, \
                auto_now_add=True)

    def __unicode__(self):
        return self.title

class Logdetail(models.Model):
    worklog     = models.ForeignKey(Worklog)
    log_date    = models.DateField('Date')
    log_start   = models.TimeField('Start Time')
    log_end     = models.TimeField('End Time')
    log_hours   = models.DecimalField('Total Hours', \
                    max_digits=19, decimal_places=2)
    log_amount  = models.DecimalField('Line Amount', \
                    max_digits=19, decimal_places=2)
    comments    = models.TextField()

    def  __unicode__(self):
        return self.comments
    
