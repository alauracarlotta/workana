from django.shortcuts import redirect, render
from apps.core.forms import ClientForm, ImmobileForm, RegisterLocationForm
from .models import Immobile, ImmobileImages

""" def home(request):
    return render(request, 'index.html') """

def list_location(request):
    immobiles = Immobile.objects.filter(is_locate=False)
    context = {
        'immobiles': immobiles
    }
    return render(request, 'list-location.html', context)

def form_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-location')
    return render(request, 'form-client.html', {'form': form})

def form_immobile(request):
    form = ImmobileForm()
    if request.method == 'POST':
        form = ImmobileForm(request.POST, request.FILES)
        if form.is_valid():
            immobile = form.save()
            files = request.FILES.getlist('immobile')
            if files:
                for file in files:
                    ImmobileImages.objects.create(
                        immobile = immobile,
                        image = file
                    )
            return redirect('list-location')
    return render(request, 'form-immobile.html', {'form': form})

def form_location(request, id):
    get_locate = Immobile.objects.get(id = id)
    form = RegisterLocationForm()
    
    if request.method == 'POST':
        form = RegisterLocationForm(request.POST)
        if form.is_valid():
            location_form = form.save(commit = False)
            location_form.immobile = get_locate
            location_form.save()

            rented_immobile = Immobile.objects.get(id = id)
            rented_immobile.is_locate = True
            rented_immobile.save()

            return redirect('list-location')

    context = {'form': form, 'location': get_locate}
    return render(request, 'form-location.html', context)

def reports(request):
    immobile = Immobile.objects.all()
    return render(request, 'reports.html', {'immobiles': immobile})