# Generated by Django 2.0.7 on 2018-07-30 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0007_auto_20180729_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicanalysisrunmodel',
            name='amountRetrieved',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='basicanalysisrunmodel',
            name='timeFrameInMinutes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='basicanalysisrunmodel',
            name='totalToRetrieve',
            field=models.IntegerField(default=0),
        ),
    ]