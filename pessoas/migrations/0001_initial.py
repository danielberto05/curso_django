# Generated by Django 3.0.3 on 2020-02-13 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1)),
                ('nome', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=15)),
                ('foto', models.ImageField(upload_to='fotos_presos')),
                ('telefone', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pessoas.Telefone')),
            ],
        ),
    ]
