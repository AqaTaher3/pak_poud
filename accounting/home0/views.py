from django.shortcuts import render, redirect, get_object_or_404
from customer0.models import Moshtary
from chek0.models import Chek
from django.db.models import Q



# href="{% url'customers:update' Customer.id %}
# href="/update/{{Customer.id}}


def home(request):

    kole_moshtari_ha = Moshtary.objects.all()
    customer_count = Moshtary.objects.all().count()
    tede_moshtari = 15
    content = ({'kole_moshtari_ha': kole_moshtari_ha, 'tede_moshtari':customer_count})
    return render(request, 'home0/home.html', content)
