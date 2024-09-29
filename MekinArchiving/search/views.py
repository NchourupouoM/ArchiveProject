from search.forms import SearchForm
from archives.models import Archive
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render

def searchDocument(request):
    query = None
    results = []
    search_form = SearchForm()

    if 'query' in request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            results = Archive.published.annotate(
                search = SearchVector('titre','metadonnees'),
            ).filter(search=query)

    return render(request=request, template_name="search/search_result.html",context={"search_form":search_form,'query':query, 'results':results})