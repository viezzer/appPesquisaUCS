# Generated by Django 4.2.1 on 2023-06-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appPesquisa", "0006_alter_projeto_descricao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projeto", name="criado_em", field=models.DateField(),
        ),
    ]
