# Generated by Django 3.2 on 2021-05-04 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('munice', '0003_alter_prukaz_skupiny'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategorie',
            options={'ordering': ['oznaceni_kategorie'], 'verbose_name': 'Typy produktů', 'verbose_name_plural': 'Typy produktů'},
        ),
    ]
