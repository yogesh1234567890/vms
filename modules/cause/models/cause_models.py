from django.db import models


class cause(models.Model):
    class Meta:
        db_table = 'tbl_cause'
        verbose_name_plural = 'causes'

    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(auto_now=False)
    volunteer_no = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return ('%s' % (self.name))