from django.db import models

# Create your models here.


class Profile(models.Model):
    stud_name = models.CharField(max_length=200)
    stud_id = models.FloatField()
    desc = models.TextField()
    cgpa = models.FloatField()
    email = models.EmailField()
    password = models.CharField(max_length=200, null=True)

    class Meta:
        ordering=('stud_id',)

    def __str__(self):
        return self.stud_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name


class Project(models.Model):
    profile = models.ForeignKey(Profile,related_name='projects', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='projects', blank=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Internship(models.Model):
    profile = models.ForeignKey(Profile,related_name='internships', on_delete=models.CASCADE)
    company = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150)
    desc = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.company+' '+self.job_title
