from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterForm, EditForm
from django.contrib.auth.forms import SetPasswordForm
# from learning.models import student
# from learning.form import PostForm




def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'register.html')
def User_login(request):
    return render(request,'login.html')
def personal(request):
    return render(request,'personal.html')
def User_logout(request):
    return render(request,'home.html')
def coursestart(request):
    return render(request,'coursestart.html')
def class1(request):
    return render(request,'class1.html') 
def lesson0(request):
    return render(request,'lesson0.html')  
def lesson_1(request):
    return render(request,'lesson1_1.html')
def lesson_2(request):
    return render(request,'lesson1_2.html')
def lesson_3(request):
    return render(request,'lesson1_3.html')
def lesson_4(request):
    return render(request,'lesson2_1.html')
def lesson_5(request):
    return render(request,'lesson2_2.html')
def lesson_6(request):
    return render(request,'lesson2_3.html')
def lesson_7(request):
    return render(request,'lesson2_4.html')  
def lesson_8(request):
    return render(request,'lesson2_5.html')
def lesson_9(request):
    return render(request,'lesson3_1.html')
def lesson_10(request):
    return render(request,'lesson3_2.html')
def lesson_11(request):
    return render(request,'lesson3_3.html')
def lesson_12(request):
    return render(request,'lesson3_4.html')
def lesson_13(request):
    return render(request,'lesson4_1.html')
def lesson_14(request):
    return render(request,'lesson4_2.html')
def lesson_15(request):
    return render(request,'lesson4_3.html')
def lesson_16(request):
    return render(request,'lesson3_5.html')
   


def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        # 如果希望註冊完馬上登入可加入，若無需求可不加
        # ------------------------------------
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        # ------------------------------------
        return HttpResponseRedirect('/coursestart/')
  else:
    form = RegisterForm()
  return render(request,'register.html',{'form':form,})

# 在learning/views.py 新增 User_login
def User_login(request):
    # 如果已經登入，跳至個人頁面
    # 此階段為空白頁面
    if request.user.is_authenticated:
        return HttpResponseRedirect('/coursestart/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        # 如果User是已註冊的就login
        if user is not None: 
            login(request, user)           
            return HttpResponseRedirect('/coursestart/')
        else:
            # 如果登入失敗，則丟出錯誤訊息
            error_message = "帳號不存在或是密碼錯誤，請再試一次"
            return render(request,'login.html',{'error_message':error_message})
    return render(request,'login.html')

# 在learning/views.py再加入User_logout function
def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# 在 views.py 中新增 personal function
# 此為修改普通資料的 view
def personal(request):
    instance = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = EditForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = EditForm(instance=instance)
    return render(request, 'personal.html',
        {
            'account': request.user.username,
            'form':form
        })

def reset_password(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    form = SetPasswordForm(user=request.user, data=request.POST)
    if form.is_valid():
        form.save()
        #update_session_auth_hash(request, form.user)
        return HttpResponseRedirect('/logout/')
    return render(request, 'reset.html',{ 'form':form })

# 留言板
# def lesson0(request):  
# 	students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
# 	return render(request, "lesson0.html", locals())
	
# def post(request):
# 	if request.method == "POST":		#如果是以POST方式才處理
# 		mess = request.POST['username'] #取得表單輸入資料
# 	else:
# 		mess="表單資料尚未送出!"	
# 	return render(request, "post.html", locals())
	
# def post1(request):  #新增資料，資料不作驗證
# 	if request.method == "POST":	  #如果是以POST方式才處理
# 		cName = request.POST['cName'] #取得表單輸入資料
		
# 		cAddr =  request.POST['cAddr']
# 		#新增一筆記錄
# 		unit = student.objects.create(cName=cName, cAddr=cAddr) 
# 		unit.save()  #寫入資料庫
# 		return redirect('/lesson0/')	
# 	else:
# 		message = '請輸入資料(資料不作驗證)'
# 	return render(request, "post1.html", locals())	
	
# def post2(request):  #新增資料，資料必須驗證
# 	if request.method == "POST":  #如果是以POST方式才處理
# 		postform = PostForm(request.POST)  #建立forms物件
# 		if postform.is_valid():			#通過forms驗證
# 			cName = postform.cleaned_data['cName'] #取得表單輸入資料
			
# 			cAddr =  postform.cleaned_data['cAddr']
# 			#新增一筆記錄
# 			unit = student.objects.create(cName=cName, cAddr=cAddr) 
# 			unit.save()  #寫入資料庫
# 			message = '已儲存...'
# 			return redirect('/lesson0/')	
# 		else:
# 			message = '驗證碼錯誤！'	
# 	else:
# 		message = '姓名、內容必須輸入！'
# 		postform = PostForm()
# 	return render(request, "post2.html", locals())		
		
# def delete(request,id=None):  #刪除資料
# 	if id!=None:
# 		if request.method == "POST":  #如果是以POST方式才處理
# 			id=request.POST['cId'] #取得表單輸入的編號
# 		try:
# 			unit = student.objects.get(id=id)  
# 			unit.delete()
# 			return redirect('/lesson0/')
# 		except:
# 			message = "讀取錯誤!"			
# 	return render(request, "delete.html", locals())	
	
# def edit(request,id=None,mode=None):  
# 	if mode == "edit":  # 由 edit.html 按 submit
# 		unit = student.objects.get(id=id)  #取得要修改的資料記錄	
# 		unit.cName=request.GET['cName']
		
# 		unit.cAddr=request.GET['cAddr']		
# 		unit.save()  #寫入資料庫
# 		message = '已修改...'
# 		return redirect('/lesson0/')	
# 	else: # 由網址列
# 		try:
# 			unit = student.objects.get(id=id)  #取得要修改的資料記錄
# 			strdate=str(unitcAddr)
# 			strdate2=strdate.replace("年","-")
# 			strdate2=strdate.replace("月","-")
# 			strdate2=strdate.replace("日","-")
# 			unit.cAddry = strdate2
# 		except:
# 			message = "此 id不存在！"	
# 		return render(request, "edit.html", locals())	
		
# def edit2(request,id=None,mode=None):
#     if mode == "load":  # 由 index.html 按 編輯二 鈕
#       unit = student.objects.get(id=id)  #取得要修改的資料記
#       strdate=str(unit.cAddr)
#       strdate2=strdate.replace("年","-")
#       strdate2=strdate.replace("月","-")
#       strdate2=strdate.replace("日","-")
#       unit.cAddry = strdate2		
#       return render(request, "edit2.html", locals())
#     elif mode == "save": # 由 edit2.html 按 submit		
#       unit = student.objects.get(id=id)  #取得要修改的資料記錄	
#       unit.cName=request.POST['cName']
      
#       unit.cAddr=request.POST['cAddr']		
#       unit.save()  #寫入資料庫
#       message = '已修改...'
#       return redirect('/lesson0/')
	  
# def postform(request):  #新增資料，資料必須驗證
# 	postform = PostForm()  #建立PostForm物件
# 	return render(request, "postform.html", locals())		  


#忘記密碼

