from search.forms import SearchForm
from archives.models import Archive
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.shortcuts import render

def searchDocument(request):
    query = None
    results = []
    search_form = SearchForm()

    if 'query' in request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']

            vector_search = SearchVector('titre','metadonnees')
            query_search = SearchQuery(query)

            results = Archive.published.annotate(
                search = vector_search ,rank =SearchRank(vector_search, query_search)
            ).filter(search=query_search).order_by('-rank')

    return render(request=request, template_name="search/search_result.html",context={"search_form":search_form,'query':query, 'results':results})