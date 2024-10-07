import json

from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from urlsAndViews.departments.models import Department


def index(request):
    # url = reverse('redirect-view')
    # url_lazy = reverse_lazy('redirect-viewa')
    return HttpResponse(f"<h1>hcwbeuhbf</h1>")


def view_with_name(request, variable):  # should be named the same way as in the urls
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request, 'departments/name_template.html', {"variable": variable})


def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args}, Kwargs: {kwargs}</h1>")


def view_with_int_pk(request, pk):
    # return HttpResponse(json.dumps({"pk": pk}), content_type="application/json")
    return JsonResponse({"pk": pk})   # option 2 makes same thing with abstraction


def view_with_slug(request, pk, slug):
    # OPTION 1 for 404
    # department = Department.objects.filter(pk=pk, slug=slug)
    #
    # if not department:
    #     raise Http404

    # OPTION 2
    department = get_object_or_404(Department, pk=pk, slug=slug)

    raise Http404

    # return HttpResponse(f"<h1>Department from slug: {department}</h1>")


def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")


def redirect_to_softuni(request):
    return redirect('https://softuni.bg')


def redict_to_view(request):
    # redirect('http://localhost:8000/numbers/')  breaks abstraction
    # redirect(index)   # breaks SR if view is from another app
    return redirect('numbers', pk=2)  # Best option
