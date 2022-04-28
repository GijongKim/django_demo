from django.contrib import admin
from .models import Post

class PostAdminConfig(admin.ModelAdmin):
    # readonly_fields = ["title"]
    # 관리자 페이지에서 제목은 수정하지 못하게 한 거임. 
    list_filter = ['title']
    
admin.site.register(Post,PostAdminConfig)