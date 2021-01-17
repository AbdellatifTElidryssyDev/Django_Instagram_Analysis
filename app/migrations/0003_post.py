# Generated by Django 3.1.3 on 2020-11-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201106_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(verbose_name='いいね')),
                ('comments', models.IntegerField(verbose_name='コメント')),
                ('label', models.CharField(max_length=200, verbose_name='投稿日')),
            ],
        ),
    ]
