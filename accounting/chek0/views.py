from django.shortcuts import render, redirect, get_object_or_404
from .models import Czech
from .forms import CreateCzechForm
from customer0.models import Client
from factor0.models import Invoice
from django.db.models import Q


def kole_chek_ha(request):

    chek_ha = Czech.objects.all()
    chek_count = len(chek_ha)
    q_chek = request.GET.get('q_chek') if request.GET.get('q_chek') else ''
    cheks = chek_ha.filter(Q(sayad__icontains=q_chek)|Q(chec_bearer__name__icontains=q_chek))

    content = ({'chek_ha':cheks, 'chek_count':chek_count})
    return render(request, 'chek0/home.html', content)


def chek_profile(request, id):
    chek = get_object_or_404(Czech, id=id)

    content = {'chek':chek}
    return render(request, 'chek0/profile.html', content)


def create_chek(request):
    if request.method == "POST":
        form = CreateCzechForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chek:home')
        context = {'form':form}
        return render(request, 'create.html', context)

    else:
        form = CreateCzechForm()
        return render(request, "create.html", {"form":form})


def update_chek(request, id):
    chek = Czech.objects.get(id=id)
    form = CreateCzechForm(instance=chek)
    if request.method == "POST":
        form = CreateCzechForm(request.POST, instance=chek)
        if form.is_valid():
            form.save()
            return redirect('chek:home')
        return redirect('chek:update', id)

    else:
        form = CreateCzechForm(instance=chek)
        context = {'form':form}
        CreateCzechForm(instance=chek)
        return render(request, "update.html", context)


def delete_chek(request, id):
    chek = Czech.objects.get(id=id)
    if request.method == 'POST':
        chek.delete()
        return redirect('chek:home')
    return render(request, 'delete.html', {'obj':chek})


def daryafti_profile(request, factor_id):

    factors = Invoice.objects.all()
    factor = factors.get(id = factor_id)
    factor_number = factor.invoice_number
    received = factor.received
    cheks = received.chek.all()
    cash = received.cash
    date = received.date
    updated = received.date
    hesab_id = received.id
    kole_daryafti = received.total_received



    context = {'factor':factor,'cash':cash, 'cheks':cheks, 'date':date, 'updated':updated,
               'hesab_id':hesab_id, 'kole_daryafti':kole_daryafti}
    return render(request, "chek0/hesab_profile.html", context)
