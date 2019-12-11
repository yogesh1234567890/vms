# Generated by Django 2.2.7 on 2019-12-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('volunteer_no', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'causes',
                'db_table': 'tbl_cause',
            },
        ),
    ]
