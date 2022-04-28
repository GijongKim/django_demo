from django.urls import path, include # include 함수로 landing에 연결을 해줄 수 있음.
from . import views # 상대경로로 저장을 해 줘야 함.

app_name = "blog"
urlpatterns = [
    path('',views.index), # 아무것도 입력안했을 때, views의 index를 실행시켜준다.
    path('second/',views.article),
    path('post-write/', views.blog_post_write),
    path('home/', views.blog_home, name="home"),
    path('post-view/<int:post_id>/', views.blog_post_view, name="detail"),
    path('post-edit/<int:post_id>/', views.blog_post_update),
    path('post-delete/<int:post_id>/',views.blog_post_delete),
]