# Generated by Django 3.2.9 on 2021-12-18 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statictemplate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cEmail',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cSubject',
            field=models.CharField(max_length=100),
        ),
    ]
