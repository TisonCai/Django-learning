# Generated by Django 2.2.4 on 2019-09-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='text',
            field=models.CharField(default='', max_length=200, verbose_name='学习条目'),
        ),
        migrations.AddField(
            model_name='topic',
            name='text',
            field=models.CharField(default='', max_length=200, verbose_name='学习主题'),
        ),
    ]
