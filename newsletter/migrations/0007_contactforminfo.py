# Generated by Django 3.0.3 on 2020-02-25 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newsletter', '0006_delete_contactforminfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=300)),
                ('student_age', models.CharField(max_length=300)),
                ('student_email', models.CharField(max_length=300)),
            ],
        ),
    ]
