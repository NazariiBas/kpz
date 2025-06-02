# app_blog /views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article

# Створіть свої представлення тут.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
    
def index(request):
    articles = Article.objects.all()
    return render(request, 'app_blog/index.html', {'articles': articles})