# Generated by Django 3.1.3 on 2020-12-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/files'),
        ),
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]