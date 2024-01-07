from django.shortcuts import render, redirect, get_object_or_404
from customer0.models import Moshtary
from chek0.models import Chek
from factor0.models import Tage, Foroosh
from django.db.models import Q



# href="{% url'customers:update' Customer.id %}
# href="/update/{{Customer.id}}


def home(request):

    kole_moshtari_ha = Moshtary.objects.all()
    customer_count = Moshtary.objects.all().count()
    chek_be_nam_nashode = Chek.objects.filter(Q(ki_daryaft_kard__exact='') | Q(ki_daryaft_kard__isnull=True)).count()
    magsad_nashode = Chek.objects.filter(Q(magsad__isnull=False) | Q(ki_daryaft_kard__exact='')
                                              | Q(ki_daryaft_kard__isnull=True)).count()

    factor_haye_baz = len(Foroosh.objects.filter(baste_shod = 'baz'))
    content = ({'kole_moshtari_ha': kole_moshtari_ha, 'tede_moshtari':customer_count,
                'chek_be_nam_nashode':chek_be_nam_nashode, 'magsad_nashode':magsad_nashode,'factor_haye_baz':factor_haye_baz})
    return render(request, 'home0/home.html', content)
