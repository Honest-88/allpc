# Generated by Django 4.0.4 on 2022-05-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_filelink_four_article_filelink_one_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='File_hoster_name1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='article',
            name='File_hoster_name2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='article',
            name='File_hoster_name3',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='article',
            name='File_hoster_name4',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]
