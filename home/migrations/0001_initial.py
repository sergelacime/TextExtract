# Generated by Django 4.2.3 on 2023-07-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomPlan', models.CharField(max_length=300)),
                ('text', models.CharField(max_length=1000000000)),
                ('file', models.FileField(default='', upload_to='archives/')),
            ],
            options={
                'verbose_name_plural': 'file',
            },
        ),
    ]
