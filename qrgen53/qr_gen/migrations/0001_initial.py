# Generated by Django 4.0.6 on 2022-08-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('date_created', models.DateField(auto_now=True)),
                ('base_url', models.TextField()),
                ('type_qr', models.TextField()),
                ('light', models.CharField(default='white', max_length=15)),
                ('dark', models.CharField(default='black', max_length=15)),
                ('stats', models.IntegerField(default=0)),
            ],
        ),
    ]
