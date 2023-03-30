from django.shortcuts import render

from django.views.generic import ListView

from .models import *

from .models import Portfolio, Men


class MenViews(ListView):
    model = Men
    template_name = "index.html"
    context_object_name = "Local"


def index(request):
    m1 = Portfolio.objects.all()
    m2 = Men.objects.all()
    contex = {
        "Portfolio": m1,
        'Local': m2
    }
    return render(request, ["index.html", "portfolio.html"], contex)


class PortfolioViews(ListView):
    model = Portfolio
    template_name = "portfolio.html"
    context_object_name = "Portfolio"


class BlogViews(ListView):
    model = Blog
    template_name = "blog.html"
    context_object_name = "Blog"
