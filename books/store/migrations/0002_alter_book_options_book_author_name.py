# Generated by Django 4.1.7 on 2023-04-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='Author', max_length=255),
        ),
    ]
