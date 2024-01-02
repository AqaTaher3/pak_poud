from django.shortcuts import render, redirect, get_object_or_404
from customer0.models import Moshtary
from chek0.models import Chek
from django.db.models import Q
from .forms import CreateMoshtaryForm


def kole_customer_ha(request):

    customers = Moshtary.objects.all()
    customer_count = Moshtary.objects.all().count()
    content = ({'customers': customers, 'customer_count':customer_count})
    return render(request, 'customer0/home.html', content)

# ki_daryaft_kard is Not blank

def customer_profile(request, pk):
    customer = get_object_or_404(Moshtary, id=pk)
    customer_cheks= Chek.objects.filter(tahvil_dahande = customer)
    chek_count= Chek.objects.filter(tahvil_dahande = customer).count()
    chek_be_nam_nashode= Chek.objects.filter(Q(tahvil_dahande = customer) &  (Q(ki_daryaft_kard__exact='') | Q(ki_daryaft_kard__isnull=True)))
    be_nam_nashode = chek_be_nam_nashode.count()
    content = {'customer':customer, 'chek_count':chek_count, 'be_nam_nashode':be_nam_nashode}
    return render(request, 'customer0/profile.html', content)



def create_customer(request):

    if request.method == "POST":
        form = CreateMoshtaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer:home')
        context = {'form': form}
        return render(request, 'create.html', context)

    else:

        form = CreateMoshtaryForm()

        return render(request, "create.html", {"form": form})



def update_customer(request, pk):
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
        return render(request, "update.html", context)



def delete_customer(request, pk):
    customer = Moshtary.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer:home')
    return render(request, 'delete.html', {'customer':customer})
