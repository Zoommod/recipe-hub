from django.shortcuts import render, get_object_or_404
from utils.recipe.test import make_recipe
from .models import Recipe, Category

def home (request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })

def recipe (request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'category': category,
    })