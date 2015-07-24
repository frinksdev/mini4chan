from django.shortcuts import render, redirect,get_object_or_404
from .models import chan, comentario
from .forms import post,comentar
from django.utils import timezone
# Create your views here.
def index(request):
	p=chan.objects.order_by("-p_date")
	return render(request,"blog/last.html",{"post":p})

def add(request):
	if request.method=="POST":
		form=post(request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog.views.index')
	else:
		form=post()
	return render(request,"blog/new.html",{"form":form})

def view_p(request,pk):
	if request.method=="POST":
		form=comentar(request.POST)
		if form.is_valid():
			comen=form.save(commit=False)
			cn=chan.objects.get(pk=pk)
			comen.post=cn
			cn.p_date=timezone.now()
			cn.save()
			comen.save()
			return redirect("blog.views.view_p", pk=pk)
	else:
		form=comentar()
		pos=get_object_or_404(chan,pk=pk)
		comment=comentario.objects.filter(post__id=pk).order_by("-p_date")
	return render(request,"blog/post.html",{"p":pos,"c":comment,"form":form})
