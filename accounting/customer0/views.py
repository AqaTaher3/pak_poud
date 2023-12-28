from django.shortcuts import render, redirect, get_object_or_404
from customer0.models import Moshtary
from chek0.models import Chek
from django.db.models import Q
from .forms import CreateMoshtaryForm


def moshtari_profile(request, pk):
    moshtari = get_object_or_404(Moshtary, pk=pk)
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

# # href="{% url'base:update' room.id %}
# # href="/update/{{room.id}}


# def update_room(request, pk):
#     room = Room.objects.get(id=pk)
#     form = CreateRoomForm(instance=room)
#     if request.method == "POST":
#         form = CreateRoomForm(request.POST, instance=room)
#         if form.is_valid():
#             form.save()
#             return redirect('base:room', pk)
#         return redirect('base:update-room', pk)

#     else:
#         form = CreateRoomForm(instance=room)
#         context = {'form': form}
#         CreateRoomForm(instance=room)
#         return render(request, "base/update_form.html", context)


# def delete_room(request, pk):
#     room = Room.objects.get(id=pk)
#     if request.method == 'POST':
#         room.delete()
#         return redirect('base:home')
#     return render(request, 'base/delete_room.html', {'obj':room})
