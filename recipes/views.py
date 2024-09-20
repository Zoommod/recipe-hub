from django.shortcuts import render, get_object_or_404, get_list_or_404
from utils.recipe.test import make_recipe
from .models import Recipe, Category

def home (request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })

def recipe (request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(category=category, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{category.name}'
    })