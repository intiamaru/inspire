# Generated by Django 3.2.6 on 2021-08-03 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='stack',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]