from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article



# Permissions enforced using @permission_required decorator

@permission_required('app_name.can_view', raise_exception=True)
def view_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

@permission_required('app_name.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        # Logic to create an article
        return redirect('article_list')
    return render(request, 'article_form.html')

@permission_required('app_name.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # Logic to edit the article
        return redirect('article_detail', pk=article.pk)
    return render(request, 'article_form.html', {'article': article})

@permission_required('app_name.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')
