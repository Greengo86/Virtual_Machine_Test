# Generated by Django 3.2.9 on 2021-11-14 11:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=150, verbose_name='Название подразделения')),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool_name', models.CharField(max_length=100, verbose_name='Пул ресурсов')),
            ],
        ),
        migrations.CreateModel(
            name='Vm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('ram', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)])),
                ('cpu', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)])),
                ('hdd', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(10)])),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vm_organization_name', to='vm.organization', verbose_name='Подразделение')),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vm_pool_name', to='vm.pool', verbose_name='Пул Ресурсов')),
            ],
        ),
    ]
