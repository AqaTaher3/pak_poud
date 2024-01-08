from django.shortcuts import render, redirect, get_object_or_404
from .models import Foroosh
from .forms import ForooshForm


def kole_factor_ha(request):

    factors = Foroosh.objects.all()
    last_factor = factors.order_by("-id")[0].shomare_factor + 1
    # factor_haye_baz = Foroosh.objects.filter(baste_shod = 'baz')
    content = ({'factors': factors, 'last_factor':last_factor, })
    return render(request, 'factor0/home.html', content)

# 'factor_haye_baz':factor_haye_baz

def factor_profile(request, id):
    factor = get_object_or_404(Foroosh, id=id)
    content = {'factor': factor}
    return render(request, 'factor0/profile.html', content)



def create_factor(request):

    if request.method == "POST":
        form = ForooshForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('factor:home')
        context = {'form': form}
        return render(request, 'create.html', context)

    else:

        form = ForooshForm()
        context = {'form': form}
        return render(request, 'create.html', context)



def update_factor(request, id):
    factor = Foroosh.objects.get(id=id)
    form = ForooshForm(instance=factor)
    if request.method == "POST":
        form = ForooshForm(request.POST, instance=factor)
        if form.is_valid():
            form.save()
            return redirect('factor:home')
        return redirect('factor:update', id)

    else:
        form = ForooshForm(instance=factor)
        context = {'form': form}
        ForooshForm(instance=factor)
        return render(request, "update.html", context)



def delete_factor(request, id):
    factor = Foroosh.objects.get(id=id)
    if request.method == 'POST':
        factor.delete()
        return redirect('factor:home')
    return render(request, 'delete.html', {'factor':factor})
