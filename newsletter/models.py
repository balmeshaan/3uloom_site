from django.db import models

# Create your models here.


class ContactFormInfo(models.Model):
    student_name = models.CharField(max_length=300)
    student_age = models.IntegerField(max_length=300)
    student_email = models.CharField(max_length=300)

    def __str__(self):
        return self.student_name


class TutorContactFormInfo(models.Model):
    tutor_name = models.CharField(max_length=300)
    tutor_subject = models.CharField(max_length=300)
    tutor_level = models.IntegerField(max_length=300)
    tutor_email = models.CharField(max_length=300)

    def __str__(self):
        return self.tutor_name


class MessageContactFormInfo(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)

    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.name