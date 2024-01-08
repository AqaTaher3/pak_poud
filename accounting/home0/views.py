from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F, Value, FloatField
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


    fac = Foroosh.objects.annotate(
        albagi_hesab=F('Mablag_kol') - F('Hesab_daryafti__kole_daryafti'))

    factor_haye_baz = fac.filter(albagi_hesab=0)


    factor_haye_baz_count = len(factor_haye_baz)


    content = ({'customers': customers, 'customers_count':customers_count,'chek_haye_kharj_nashode':chek_haye_kharj_nashode,
                'chek_be_nam_nashode':chek_be_nam_nashode, 'magsad_nashode':magsad_nashode,'fac_count':factor_haye_baz_count})
    return render(request, 'home0/home.html', content)
