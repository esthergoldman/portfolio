# Generated by Django 3.1.7 on 2021-05-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]