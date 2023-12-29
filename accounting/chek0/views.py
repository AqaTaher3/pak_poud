from django.shortcuts import render, redirect, get_object_or_404
from customer0.models import Moshtary
from chek0.models import Chek
from .forms import CreateChekForm, UpdateChekForm
from customer0.models import Moshtary
from django.db.models import Q


def create_chek(request):

    if request.method == "POST":
        form = CreateChekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
        context = {'form': form}
        return render(request, 'customer0/create.html', context)

    else:

        form = CreateChekForm()

        return render(request, "customer0/create.html", {"form": form})


def chek_profile(request, pk):
    chek = get_object_or_404(Chek, pk=pk)
    content = {'chek': chek}
    return render(request, 'cusotmer0/profile.html', content)

