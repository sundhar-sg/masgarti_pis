# Generated by Django 3.2.7 on 2021-10-13 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Intelligence', '0006_alter_user_details_db_saltvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details_db',
            name='saltvalue',
            field=models.BinaryField(),
        ),
    ]
