# Generated by Django 4.2.1 on 2023-06-05 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPesquisa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('situacao', models.CharField(max_length=100)),
                ('natureza', models.CharField(max_length=100)),
                ('criado_em', models.DateTimeField()),
            ],
        ),
    ]