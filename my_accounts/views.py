from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def sign_up(request):
    # 요청이 post인지 확인 / 그게 아니라면 get일 것.
    context = {}
    if request.method == 'POST':
    # 1. 요청받은 request에서 username이 존재하는지 &
        username = request.POST.get('username')
    # 2. 요청받은 request에서 userpassword가 존재하는지 &
    # 3. 요청받은 request에서 password와 password_check가 같은지 &
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')
        
        if (username and password and password == password_check):
            try: # error를 잡아주는 python method 'try'
                new_user = User.objects.create_user(username=username, password = password)
                auth.login(request, new_user)
                print('log in success!')
                return HttpResponseRedirect(reverse('blog_samples:home'))
            except:
                context['error'] = '이미 존재하는 id입니다.'
    # all clear = sign up 실행 - new user id로 log in까지 시켜주기.
    # 블로그 홈으로 리다이렉트 시켜주기.
    # 위 조건 중 맞지 않다면, error message를 context에 담기.
        else:
            context['error'] = '아이디와 비밀번호를 잘 못 입력하셨습니다.'
    
     
    return render(request, 'my_accounts/sign_up.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect("blog_samples:home")
    context={}
    # 요청이 post인지 확인
    if request.method == 'POST':
    # id 입력받은 것이 있는지? ok / password 입력받은 것이 있는지? ok 
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if (username and password):
    # password check? ok --- 추가적으로 필요한 함수
            user = auth.authenticate(
                request,
                username = username, password = password
            )
            if user:
                auth.login(request, user)
        # login ok
                return redirect('blog_samples:home')
        # redirect ok
        
    # all clear > login
            else:
                context['error'] = 'login failed'
    # failed > context에 error message 담아주기.
    else:
        context['error'] = 'put in your id & password'
    
    return render(request, 'my_accounts/login.html', context)

def logout(request):
    # 요청이 post인지 확인!
    # if request.method == "POST":
    auth.logout(request)
    # 로그아웃 o / 
    return redirect('blog_samples:home')
    # redirect o