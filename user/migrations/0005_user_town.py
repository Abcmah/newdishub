# Generated by Django 4.0.3 on 2022-03-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='town',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]