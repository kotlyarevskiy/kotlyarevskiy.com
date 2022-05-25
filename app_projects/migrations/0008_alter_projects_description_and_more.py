# Generated by Django 4.0.4 on 2022-05-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0007_alter_projects_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description_uk',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
    ]
