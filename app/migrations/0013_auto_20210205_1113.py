# Generated by Django 3.0 on 2021-02-05 17:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210205_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblactionmaster',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tblactionmaster',
            name='actionID',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='tblappealmaster',
            name='appealStructure',
            field=models.CharField(blank=True, choices=[('CIRP', 'CIRP'), ('Optional', 'Optional'), ('Individual', 'Individual')], db_column='appealStructure', max_length=25, null=True),
        ),
    ]