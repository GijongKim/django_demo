from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Post

def index(request):
    return HttpResponse('<h1>여기는 블로그 첫 페이지</h1>')

def article(request):
    return HttpResponse('<h1>안녕하세요 김기종입니다.</h1>')

def blog_post_write(request):
    if request.method == "GET": # 요청의 method가 get이던 post건 다 띄우지말고, get method일 경우에만 써라.
        return render(request, 'blog/create.html') # 블로그 app안에 create.html이라는 template을 불러오겠다.
    if request.method == "POST":
        new_post = Post()
        new_post.title = request.POST["title"] # post로 오는 것이 dict type임. 접근하기 위해서 대괄호로.
        new_post.content = request.POST["content"]
        if request.FILES.get("image"):
            new_post.head_image = request.FILES.get("image")
        print(new_post.head_image)
        new_post.save()
        return HttpResponseRedirect(reverse("blog:home"))
    
def blog_home(request):
    blog_posts = Post.objects.all()
    context = {
        "blog_posts_key":blog_posts,
        "dummy":"i am dummy"
    }
    return render(request, 'blog/index.html',context)
    # render 뒤의 ''은 앞에 슬래시가 없다. 템플릿 폴더 안에서 찾는 것.
    # 있으면 실제 url로 들어가서 찾는 것.
    
def blog_post_view(request, post_id):
    a_post = Post.objects.get(id=post_id)
    
    context = {
        "id" : a_post.id,
        "title" : a_post.title,
        "content" : a_post.content,
    }
    
    if a_post.head_image:
        context["image"]=a_post.head_image
        
    return render(request, 'blog/detail.html', context)

def blog_post_update(request, post_id):
    a_post = Post.objects.get(id = post_id)
    context = {
        "id" : a_post.id,
        "title" : a_post.title,
        "content" : a_post.content,
    }
    if request.method == "GET":
        return render(request, 'blog/edit.html', context)
    if request.method == "POST":
        a_post.title = request.POST["title"] 
        # html input tag에 name이 title임. 그걸 가져옴!
        a_post.content = request.POST["content"]
        a_post.save() # 저장 필수.
        return HttpResponseRedirect(f'/blog/post-view/{post_id}/')
 
 
def blog_post_delete(request, post_id):
    if request.method == "POST": 
        a_post = Post.objects.get(id = post_id)
        a_post.delete()
        # 삭제하고는 저장 안해도 됨. 삭제 후 저장되는 것.
        return HttpResponseRedirect('/blog/home/')
        # CRUD 중 Delete 기능 함수.