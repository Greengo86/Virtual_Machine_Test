from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import DO_NOTHING


class Vm(models.Model):
    pool = models.ForeignKey('Pool', on_delete=DO_NOTHING,
                             verbose_name='Пул Ресурсов', related_name='Vm_pool_name', blank=True, null=True)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE,
                                     verbose_name='Подразделение', related_name='Vm_organization_name')
    name = models.TextField()
    ram = models.IntegerField(default=1,
                              validators=[
                                  MaxValueValidator(8),
                                  MinValueValidator(1)
                              ])
    cpu = models.IntegerField(default=1,
                              validators=[
                                  MaxValueValidator(8),
                                  MinValueValidator(1)
                              ])
    hdd = models.IntegerField(default=10,
                              validators=[
                                  MaxValueValidator(100),
                                  MinValueValidator(10)
                              ])

    def __str__(self):
        return self.name


class Pool(models.Model):
    pool_name = models.CharField(max_length=100, verbose_name='Пул ресурсов')

    def __str__(self):
        return self.pool_name


class Organization(models.Model):
    organization_name = models.CharField(max_length=150, verbose_name='Название подразделения')

    def __str__(self):
        return self.organization_name
