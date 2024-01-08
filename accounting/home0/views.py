from django.shortcuts import render, redirect, get_object_or_404
from customer0.models import Moshtary
from chek0.models import Chek
from factor0.models import Tage, Foroosh
from django.db.models import Q



# href="{% url'customers:update' Customer.id %}
# href="/update/{{Customer.id}}


def home(request):

    customers = Moshtary.objects.all()
    factors = Foroosh.objects.all()
    cheks = Chek.objects.all()

    customers_count = len(customers)

    chek_haye_kharj_nashode = len(cheks.filter(Q(magsad__exact='') | Q(magsad__isnull=True)))

    chek_be_nam_nashode = len(cheks.filter(Q(ki_daryaft_kard__exact='') | Q(ki_daryaft_kard__isnull=True)))

    magsad_nashode = Chek.objects.filter(Q(magsad__isnull=False) | Q(ki_daryaft_kard__exact='')
                                              | Q(ki_daryaft_kard__isnull=True)).count()

    factor_haye_baz = len(factors.filter(baste_shod = 'baz'))
    factor_haye_baz_count = len(factors.filter(baste_shod = 'baz'))


    # most_daftari = (factors.order_by("-updated")[0]).shomare_factor
    # most_daftari = factor_haye_baz.order_by("-albagi_hesab")[0].shomare_factor







    content = ({'customers': customers, 'customers_count':customers_count,'most_daftari':most_daftari,'chek_haye_kharj_nashode':chek_haye_kharj_nashode,
                'chek_be_nam_nashode':chek_be_nam_nashode, 'magsad_nashode':magsad_nashode,'factor_haye_baz':factor_haye_baz_count})
    return render(request, 'home0/home.html', content)
