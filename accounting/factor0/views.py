from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice, Roll
from customer0.models import Client
from .forms import CreateInvoiceForm, CreateRollForm
from django.db.models import Q

from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView


def kole_factor_ha(request):

    factor_ha = Invoice.objects.all()
    q_factor = request.GET.get("q_factor") if request.GET.get("q_factor") else ''
    factors = factor_ha.filter(Q(invoice_number__icontains=q_factor)|Q(client__name__icontains=q_factor))
    content = ({'factors': factors })
    return render(request, 'factor0/home.html', content)

# 'factor_haye_baz':factor_haye_baz

def factor_profile(request, id):
    factor = get_object_or_404(Invoice, id=id)
    content = {'factor': factor}
    return render(request, 'factor0/profile.html', content)


def create_factor(request):

    if request.method == "POST":
        form = CreateInvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('factor:home')
        context = {'form': form}
        return render(request, 'create.html', context)

    else:

        form = CreateInvoiceForm()
        context = {'form': form}
        return render(request, 'create.html', context)

class InvoiceUpdateView(UpdateView):
    model = Invoice
    form_class = CreateInvoiceForm
    template_name = 'update.html'
    success_url = 'factor:home'


def update_factor(request, id):
    factor = Invoice.objects.get(id=id)
    form = CreateInvoiceForm(instance=factor)
    if request.method == "POST":
        form = CreateInvoiceForm(request.POST, instance=factor)
        if form.is_valid():
            form.save()
            return redirect('factor:home')
        return redirect('factor:update', id)

    else:
        form = CreateInvoiceForm(instance=factor)
        context = {'form': form}
        CreateInvoiceForm(instance=factor)
        return render(request, "update.html", context)


def delete_factor(request, id):
    factor = Invoice.objects.get(id=id)
    if request.method == 'POST':
        factor.delete()
        return redirect('factor:home')
    return render(request, 'delete.html', {'factor':factor})


def tage_haye_factor(request, factor_id):
    factors = Invoice.objects.get(id = factor_id)
    tage_ha = factors.roll.all()
    context = {'tage_ha':tage_ha}
    return render(request, 'factor0/tegefactor.html', context)


def mojoodi_anbar(request):

    tage_ha = Roll.objects.all()

    content = ({'tage_ha':tage_ha,  })
    return render(request, 'factor0/anbar.html', content)

class RollCreateView(CreateView):
    model = Roll
    form_class = CreateRollForm
    template_name = 'create.html'
    success_url = 'factor:anbar'
