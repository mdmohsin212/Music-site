from django.shortcuts import render, redirect
from Musicians.forms import MusicianForm
from Musicians.models import MusicianModel

# Create your views here.

def musicians(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            form = MusicianForm()
    else:
        form = MusicianForm()
    return render(request, 'musician.html', {'form':form})

def delete(request, id):
    MusicianModel.objects.get(pk=id).delete()
    return redirect('home')

def edit_musician(request, id):
    musician = MusicianModel.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'musician.html', {'form':musician_form})
    