from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=25) # 약 6만 text를 작성할 수있는 기능. (char field)꼭 최대길이를 명시 해 줘야함.
    content = models.TextField()
    head_image = models.ImageField(upload_to = 'blog/images/%Y/%m/%d/%H', 
                                   blank = True, null = True) # Pillow pip install 해야함. 이미지 관리해주는 것. / 빈 값은 True로, 에러를 없애주기.
    created_at = models.DateTimeField(auto_now_add = True) # 글이 작성 됐을 때, 자동적으로 해당 시간이 입력되게 해주는 속성.
    updated_at = models.DateTimeField(auto_now = True) # 수정 즉시 반영
    
    # 순서, 먼저 클래스 상속해주고, settings.py에 앱 들어가있는지 확인하는 것
    def __str__(self):
        return f"제목은 {self.title} 내용은 {self.content}"