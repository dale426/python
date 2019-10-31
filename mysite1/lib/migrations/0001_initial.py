# Generated by Django 2.2.6 on 2019-10-29 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('pub_house', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
