from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Article
from django.urls import reverse

def index(request):
	latest_list = Article.objects.order_by("-pub_date")[:7]
	return render(request, 'articles/articles.html', {"latest_list": latest_list})

def detail(request, art_id):
	try:
		art = Article.objects.get(id = art_id)
	except:
		raise Http404("Article does not exist )=")
	comments_list = art.comment_set.order_by("id")
	return render(request, 'articles/detail.html', {"article": art, "comments_list": comments_list})

def leave_comment(request, art_id):
	try:
		art = Article.objects.get(id = art_id)
	except:
		raise Http404("Article does not exist )=")
	art.comment_set.create(author = request.POST['full_name'], com_text = request.POST['text'])
	return HttpResponseRedirect(reverse('articles:detail', args = (art.id,)))