from django.shortcuts import render, redirect, get_object_or_404
from customer0.models import Client
from chek0.models import Czech
from django.db.models import Q
from .forms import CreateClientForm


def customer_home(request):

    customers = Client.objects.all()
    customers_count = len(customers)

    content = ({'customers': customers, 'customer_count':customers_count})
    return render(request, 'customer0/home.html', content)

# holder is Not blank

def customer_profile(request, pk):
    customer = get_object_or_404(Client, id=pk)
    customer_cheks= Czech.objects.filter(chec_bearer = customer)
    chek_count= Czech.objects.filter(chec_bearer = customer).count()
    chek_haye_daryaft_nashode= Czech.objects.filter(Q(chec_bearer = customer) &  (Q(holder__exact='') | Q(holder__isnull=True)))
    be_nam_nashode = chek_haye_daryaft_nashode.count()
    content = {'customer':customer, 'chek_count':chek_count, 'be_nam_nashode':be_nam_nashode}
    return render(request, 'customer0/profile.html', content)



def create_customer(request):

    if request.method == "POST":
        form = CreateClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer:home')
        context = {'form': form}
        return render(request, 'create.html', context)

    else:

        form = CreateClientForm()

        return render(request, "create.html", {"form": form})



def update_customer(request, pk):
    customer = Client.objects.get(pk=pk)
    form = CreateClientForm(instance=customer)
    if request.method == "POST":
        form = CreateClientForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer:home')
        return redirect('customer:update', pk)

    else:
        form = CreateClientForm(instance=customer)
        context = {'form': form}
        CreateClientForm(instance=customer)
        return render(request, "update.html", context)



def delete_customer(request, pk):
    customer = Client.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer:home')
    return render(request, 'delete.html', {'customer':customer})
