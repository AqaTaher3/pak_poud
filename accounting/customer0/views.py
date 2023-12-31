from django.shortcuts import render, redirect, get_object_or_404
from customer0.models import Moshtary
from chek0.models import Chek
from django.db.models import Q
from .forms import CreateMoshtaryForm


def kole_moshtari_ha(request):

    moshtari_ha = Moshtary.objects.all()
    customer_count = Moshtary.objects.all().count()
    content = ({'moshtari_ha': moshtari_ha, 'customer_count':customer_count})
    return render(request, 'customer0/home.html', content)



def moshtari_profile(request, pk):
    customer = get_object_or_404(Moshtary, id=pk)
    content = {'customer': customer}
    return render(request, 'customer0/profile.html', content)



def create_moshtari(request):

    if request.method == "POST":
        form = CreateMoshtaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer:home')
        context = {'form': form}
        return render(request, 'customer0/create.html', context)

    else:

        form = CreateMoshtaryForm()

        return render(request, "customer0/create.html", {"form": form})



def update_moshtari(request, pk):
    customer = Moshtary.objects.get(pk=pk)
    form = CreateMoshtaryForm(instance=customer)
    if request.method == "POST":
        form = CreateMoshtaryForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer:home')
        return redirect('customer:update', pk)

    else:
        form = CreateMoshtaryForm(instance=customer)
        context = {'form': form}
        CreateMoshtaryForm(instance=customer)
        return render(request, "customer0/update.html", context)



def delete_moshtari(request, pk):
    customer = Moshtary.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer:home')
    return render(request, 'customer0/delete.html', {'customer':customer})
