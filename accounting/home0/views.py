from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F, Value, FloatField
from customer0.models import Client
from chek0.models import Czech
from factor0.models import Roll, Invoice
from django.db.models import Q



# href="{% url'customers:update' Customer.id %}
# href="/update/{{Customer.id}}


def home(request):

    customers = Client.objects.all()
    factors = Invoice.objects.all()
    cheks = Czech.objects.all()

    customers_count = len(customers)

    chek_haye_kharj_nashode = len(cheks.filter(Q(destination__exact='') | Q(destination__isnull=True)))

    chek_haye_daryaft_nashode = len(cheks.filter(Q(holder__exact='') | Q(holder__isnull=True)))

    be_name_magsad_nashode = Czech.objects.filter(Q(destination__isnull=False) | Q(holder__exact='')
                                              | Q(holder__isnull=True)).count()


    # fac = Invoice.objects.annotate(
    #     notـreceived=F('total_price') - F('received__total_received'))

    # factor_haye_baz = fac.filter(notـreceived=0)


    # factor_haye_baz_count = len(factor_haye_baz)


    content = ({'customers': customers, 'customers_count':customers_count,'chek_haye_kharj_nashode':chek_haye_kharj_nashode,
                'chek_haye_daryaft_nashode':chek_haye_daryaft_nashode, 'be_name_magsad_nashode':be_name_magsad_nashode,})
    return render(request, 'home0/home.html', content)
