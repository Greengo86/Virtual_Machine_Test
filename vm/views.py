from django.shortcuts import render
from vm.forms import VmForm
from vm_service import VirtualMachineService


def index(request):
    if request.method == 'POST':
        form = VmForm(request.POST)
        if form.is_valid():
            service = VirtualMachineService()
            result = service.create_vm(data_form=form.cleaned_data)
            # Выводим ответ от API VirtualMachine
            return render(request, 'display_result.html', context={'message': result})
    else:
        form = VmForm()
    return render(request, 'index.html', {'form': form})
