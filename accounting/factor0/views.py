from django.shortcuts import render, redirect, get_object_or_404
from .models import FactorForoosh
from django.db.models import Q
from .forms import CreateFactorForooshForm


def kole_factor_ha(request):
    kole_factor_ha = FactorForoosh.objects.all()
    factor_count = FactorForoosh.objects.all().count()
    content = ({'kole_factor_ha': kole_factor_ha, 'factor_count':factor_count})
    return render(request, 'factor0/home.html', content)



def factor_profile(request, pk):
    factor = get_object_or_404(FactorForoosh, id=pk)
    content = {'factor': factor}
    return render(request, 'factor0/profile.html', content)



def create_factor(request):
    if request.method == "POST":
        form = CreateFactorForooshForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('factor:home')
        context = {'form': form}
        return render(request, 'factor0/create.html', context)

    else:

        form = CreateFactorForooshForm()

        return render(request, "factor0/create.html", {"form": form})



def update_factor(request, pk):
    factor = FactorForoosh.objects.get(pk=pk)
    form = CreateFactorForooshForm(instance=factor)
    if request.method == "POST":
        form = CreateFactorForooshForm(request.POST, instance=factor)
        if form.is_valid():
            form.save()
            return redirect('factor:home')
        return redirect('factor:update', pk)

    else:
        form = CreateFactorForooshForm(instance=factor)
        context = {'form': form}
        CreateFactorForooshForm(instance=factor)
        return render(request, "factor0/update.html", context)



def delete_factor(request, pk):
    factor = FactorForoosh.objects.get(id=pk)
    if request.method == 'POST':
        factor.delete()
        return redirect('factor:home')
    return render(request, 'factor0/delete.html', {'factor':factor})
