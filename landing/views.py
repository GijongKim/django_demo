from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound # httpresponse는 통신 요청이 왔을 때, 응답을 보내는 것.
# Create your views here.

def index(request):
    return render(request, "base.html")

# 추가로 한 번 해보기.
def months(request, month):
    month_list = []
    try:
    # if month >= 1 and month <=12:
    #     for m in range(1,13):
    #         month_list.append(f'{m}월')
    #     # print(month_list)
    #     return HttpResponse(month_list[month-1])  # 1월의 index값은 0이기에 1을 빼줘야 접근이 가능하다.
    # else:
    #     return HttpResponse('숫자를 1에서 12까지만 입력해주세요')
        for m in range(1,13):
            month_list.append(f'{m}월')
        # print(month_list)
        return HttpResponse(month_list[month-1])  # 1월의 index값은 0이기에 1을 빼줘야 접근이 가능하다.
    except:
        return HttpResponse('숫자를 1에서 12까지만 입력 해주세요')  # 이렇게 하면 index error가 뜨더라도, 예외처리를 해 준다.

def detail(request, name):
    users = [{'name': 'hooni', 'email': 'hooni@naver.com', 'hobby': 'running'},
             {'name': 'mina', 'email': 'mina@naver.com', 'hobby': 'dance'},
             {'name': 'yami', 'email': 'yami@naver.com', 'hobby': 'reading'},
             {'name': 'cool', 'email': 'cool@naver.com', 'hobby': 'surfing'},
             {'name': 'jack', 'email': 'jack@naver.com', 'hobby': 'golf'}]
    result = ""
    a_user = None
    for user in (users):
        if user["name"] == name:
            # result += f"<h1>{user['name']}</h1><h2>{user['email']}</h2></h3>{user['hobby']}</h3>"
            a_user = user
            break
        
    if a_user == None:
        return HttpResponseNotFound('유저를 찾을 수 없습니다.')
    
    return render(request, 'landing/users.html', a_user)
    # 템플릿 불러오는 렌더. 쓰고 랜딩안에 users.html 쓰고, a_user(data or context) 써서 그거 불러오겠다.
    
def index(request):
    context = {
        "weather_data":{
            "weather":"아주 맑음",
            "tempature":"17도",
            }, "members":['hooni','janny','jisu'] # dictionary 안에 dictionary 넣기.
    }
    
    return render(request, "base.html", context)
    # 템플릿에 데이터 넣어주려면 context자리, 즉 세번째 자리에 인자값 대입.