# Generated by Django 4.2.1 on 2023-07-10 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPesquisa', '0013_alter_projeto_situacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='data_encerramento',
            field=models.DateField(default=datetime.date(2024, 1, 1)),
            preserve_default=False,
        ),
    ]
