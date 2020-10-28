from django.contrib import admin

# Register your models here.
from .models import User   # 這邊一定要匯入User，感謝RelaxOP提醒
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class newUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'sex','email','phone','is_active','is_staff')
    list_filter = ('username','sex',)

#留言板
from django.contrib import admin
from learning.models import student

class studentAdmin(admin.ModelAdmin):
    # 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
	list_display=('id','cName','cAddr')
	list_filter=('cName','cAddr')
	search_fields=('cName',)
	ordering=('id',)
	
admin.site.register(student,studentAdmin)
