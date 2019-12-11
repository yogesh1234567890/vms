from django.db import models

class volunterSkills(models.Model):
    class Meta:
        db_table = 'mst_volunteer_skills'
        verbose_name_plural = 'volunteer skills'

    skills = models.CharField(max_length=50,null=False,default=False)

    def __str__(self):
        return (self.skills)



class volunteerRegistration(models.Model):
    class Meta:
        db_table = 'tbl_volunteerRegistration'
        verbose_name_plural = 'volunteer registration'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length = 50)
    contact_no = models.IntegerField()
    email = models.EmailField(max_length=25)
    address = models.CharField(max_length= 50)
    skills = models.ForeignKey(volunterSkills,on_delete='cascade')

    def __str__(self):
        return ('%s %s' % (self.first_name,self.last_name))