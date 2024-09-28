from django.shortcuts import render

# Create your views here.
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet

def recherche(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultats = SearchQuerySet().filter(text__contains=query)
            return render(request, 'resultats_recherche.html', {'resultats': resultats})
    else:
        form = SearchForm()
    return render(request, 'formulaire_recherche.html', {'form': form})