# Generated by Django 4.2.2 on 2023-06-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_rename_crete_time_train_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='Accuracy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='model',
            name='MacroF1',
            field=models.FloatField(null=True),
        ),
    ]