import re

from django import forms
from django.forms import Select, TextInput
from .models import Vm, Pool, Organization


class VmForm(forms.ModelForm):

    def clean_pool(self):
        pool = self.cleaned_data['pool']
        return Pool.objects.get(pk=pool)

    def clean_organization(self):
        organization = self.cleaned_data['organization']
        return Organization.objects.get(pk=organization)

    def clean_cpu(self):
        cpu = self.cleaned_data['cpu']
        if cpu < 1:
            raise forms.ValidationError("CPU cannot be less than 1")
        return cpu

    def clean_hdd(self):
        hdd = self.cleaned_data['hdd']
        if hdd < 10:
            raise forms.ValidationError("HDD cannot be less than 10 GB")
        return hdd

    def clean_ram(self):
        ram = self.cleaned_data['ram']
        if ram < 1:
            raise forms.ValidationError("RAM cannot be less than 0.01")
        return ram

    def clean_name(self):
        name = self.cleaned_data['name']
        '''Не понял какой формат нужен из скрина,но регуркой проверяю или 8 любых символов или первые 6, а остальные 2-#
        например - name = 'HHHHHH-#' или 'AAAAAAAA' Возможно не так понял и плюс форматы не все влезли на скрин. При 
        Более детальном ТЗ регулярку можно легко изменить под нужный формат'''
        match = re.search(r'^.{8}$|^.{6}-#$', name)
        if match is None:
            raise forms.ValidationError("Field Name is not correct. Please, Enter the data that match the format")
        return name

    pool = forms.ChoiceField(choices=[(pool.id, pool.pool_name) for pool in Pool.objects.all()], label='Пул', required=True)
    organization = forms.ChoiceField(choices=[(org.id, org.organization_name) for org in Organization.objects.all()],
                                     label='Подразделение', required=True)
    ram = forms.IntegerField(widget=forms.TextInput(attrs={
        'required': True,
        'min': 1,
        'max': 10,
        'step': 1,
        'value': 1,
        'type': 'number',
        'label': 'ffsgs',
    }))
    cpu = forms.IntegerField(widget=forms.TextInput(attrs={
        'required': True,
        'min': 1,
        'max': 8,
        'step': 1,
        'value': 1,
        'type': 'number',
        'label': 'sfsdg',
    }))
    hdd = forms.IntegerField(widget=forms.TextInput(attrs={
        'required': True,
        'step': 5,
        'min': 10,
        'max': 100,
        'value': 10,
        'type': 'number',
        'label': 'sfsdg',
    }))

    # Расскоментировать это для виджета с ползунком
    # ram = IntegerField(widget=RangeInput)

    class Meta:
        model = Vm
        fields = ('pool', 'organization', 'name', 'ram', 'cpu', 'hdd')
        widgets = {
            'pool': Select(attrs={'class': 'select', 'placeholder': 'Выберите Пул'}),
            'organization': Select(attrs={'class': 'select', 'placeholder': 'Выберите Организацию'}),
            'name': TextInput(attrs={'class': 'input_name', 'placeholder': 'ФОРМАТЫ: ХХХХХХХХ, ХХХХХХ-#,XXX'}),
            # Расскоментировать это для виджета с ползунком
            # 'ram': RangeInput(attrs={'class': 'ram_name'})
        }
