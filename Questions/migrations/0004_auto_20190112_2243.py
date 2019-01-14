# Generated by Django 2.1.4 on 2019-01-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0003_idolinformation_generation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idolinformation',
            old_name='name',
            new_name='romaji_name',
        ),
        migrations.AddField(
            model_name='idolinformation',
            name='kanji_name',
            field=models.CharField(default='NULL', max_length=10),
        ),
    ]
