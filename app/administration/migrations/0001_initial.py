# Generated by Django 3.2.5 on 2021-07-04 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('iic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('hosts', models.ManyToManyField(to='administration.Host')),
                ('pagegrouppage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='iic.pagegrouppage')),
            ],
        ),
    ]
