# Generated by Django 3.1.2 on 2020-10-29 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_date', models.DateField()),
                ('description', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
