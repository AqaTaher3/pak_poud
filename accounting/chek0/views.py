from django.shortcuts import render, redirect, get_object_or_404
from customer0.models import Client
from chek0.models import Czech
from .forms import CreateCzechForm
from customer0.models import Client
from django.db.models import Q


def kole_chek_ha(request):

    chek_ha = Czech.objects.all()
    chek_count = len(chek_ha)
    # chek_count = Client.objects.count()
    content = ({'chek_ha': chek_ha, 'chek_count':chek_count})
    return render(request, 'chek0/home.html', content)


def chek_profile(request, id):
    chek = get_object_or_404(Czech, id=id)
    content = {'chek': chek}
    return render(request, 'chek0/profile.html', content)


def create_chek(request):
    if request.method == "POST":
        form = CreateCzechForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chek:home')
        context = {'form': form}
        return render(request, 'create.html', context)

    else:
        form = CreateCzechForm()
        return render(request, "create.html", {"form": form})


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
        context = {'form': form}
        CreateCzechForm(instance=chek)
        return render(request, "update.html", context)


def delete_chek(request, id):
    chek = Czech.objects.get(id=id)
    if request.method == 'POST':
        chek.delete()
        return redirect('chek:home')
    return render(request, 'delete.html', {'obj':chek})
