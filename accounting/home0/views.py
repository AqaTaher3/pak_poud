from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, F, Value, FloatField

from customer0.models import Client
from chek0.models import Czech
from factor0.models import Roll, Invoice


# href="{% url'customers:update' Customer.id %}
# href="/update/{{Customer.id}}

def filter_invoices(request):

    context = {
        'open_invoices': open_invoices,
        'closed_invoices': closed_invoices,
    }

    return render(request, 'your_template.html', context)




def home(request):

    customers = Client.objects.all()
    factors = Invoice.objects.all()
    cheks = Czech.objects.all()
    customers_count = len(customers)

    # nokte ziba
    factor_baz_count = sum(1 for factor in factors if factor.is_open == "baz")

    a = []
    for factor in factors :
        if factor.is_open=="baz" :
            a.append(factor)
    sorted_factor = sorted(a, key=lambda x: x.not_received)
    b = sorted_factor[-1].not_received if sorted_factor else None


    chek_haye_kharj_nashode = len(cheks.filter(Q(destination__exact='') | Q(destination__isnull=True)))

    chek_haye_daryaft_nashode = len(cheks.filter(Q(holder__exact='') | Q(holder__isnull=True)))

    be_name_magsad_nashode = Czech.objects.filter(Q(destination__isnull=False) | Q(holder__exact='')
                                              | Q(holder__isnull=True)).count()


    content = ({'customers_count':customers_count,'chek_haye_kharj_nashode':chek_haye_kharj_nashode,'b':b,
                'chek_haye_daryaft_nashode':chek_haye_daryaft_nashode, 'be_name_magsad_nashode':be_name_magsad_nashode,
                'factor_baz_count':factor_baz_count, 'customers': customers, })
    return render(request, 'home0/home.html', content)
