from django.shortcuts import render, redirect, get_object_or_404
from customer0.models import Moshtary
from chek0.models import Chek
from django.db.models import Q
from .forms import CreateMoshtaryForm, UpdateMoshtariForm


def kole_moshtari_ha(request):

    moshtari_ha = Moshtary.objects.all()
    customer_count = Moshtary.objects.all().count()
    content = ({'moshtari_ha': moshtari_ha, 'tede_moshtari':customer_count})
    return render(request, 'customer0/home.html', content)


def moshtari_profile(request, id):
    moshtari = get_object_or_404(Moshtary, id=id)
    content = {'moshtari': moshtari}
    return render(request, 'cusotmer0/profile.html', content)


def create_moshtari(request):

    if request.method == "POST":
        form = CreateMoshtaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
        context = {'form': form}
        return render(request, 'customer0/create.html', context)

    else:

        form = CreateMoshtaryForm()

        return render(request, "customer0/create.html", {"form": form})


def update_moshtari(request, pk):
    room = Moshtary.objects.get(id=pk)
    form = UpdateMoshtariForm(instance=room)
    if request.method == "POST":
        form = UpdateMoshtariForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('base:room', pk)
        return redirect('base:update-room', pk)

    else:
        form = UpdateMoshtariForm(instance=room)
        context = {'form': form}
        UpdateMoshtariForm(instance=room)
        return render(request, "base/update_form.html", context)


def delete_moshtari(request, pk):
    room = Moshtary.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('base:home')
    return render(request, 'base/delete_room.html', {'obj':room})
