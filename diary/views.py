from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from diary.models import *
from django.contrib import messages

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        username = request.user
        diaries = Memo.objects.filter(author=username)
        context = {'diaries': diaries}
        return render(request, 'diary/home.html', context)
    else:
        return redirect('login')

def newDiary(request):
    if request.user.is_authenticated:
        return render(request, 'diary/new.html')
    else:
        return redirect('login')

def view_diary(request, id):
    if request.user.is_authenticated:
        memo = Memo.objects.filter(id=id, author=request.user).first()
        context = {'memo': memo}
        return render(request, "diary/view.html", context)
    else:
        return redirect("login")
def edit_diary(request):
    id = request.GET['diaryId']
    if request.user.is_authenticated:
        memo = Memo.objects.get(id=id, author=request.user)
        context = {'memo': memo}
        return render(request, 'diary/edit.html', context)
    else:
        return redirect('/404')

def search(request):
    keyword = request.GET['q']
    if request.user.is_authenticated:
        memo = Memo.objects.filter(author=request.user, title__icontains=keyword) | Memo.objects.filter(author=request.user, content__icontains=keyword) | Memo.objects.filter(author=request.user, created_at__icontains=keyword) | Memo.objects.filter(author=request.user, modified_at__icontains=keyword)
        print(memo)
        context = {'memo': memo, 'query': keyword}
        return render(request, 'diary/search.html', context)
    else:
        return redirect('login')


def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST['title']
            content = request.POST['content']
            user = request.user
            diary = Memo(title=title, content=content, author=user)
            diary.save()
            print(diary)
            messages.success(request, 'Your Memory is saved in our database. Now you can view it anytime & anywhere.')
            return redirect('home')
        else:
            return redirect('error')
    else:
        return redirect('login')
    
def delete_diary(request):
    if request.method == "POST":
        id = int(request.POST["diaryId"])
        Memo.objects.get(id=id, author=request.user).delete()
        messages.success(request, "Diary deleted successfully")
        return redirect("home")
    
def edit(request):
    if request.method == "POST":
        id = int(request.POST.get('id'))
        memo = Memo.objects.get(id=id)
        memo.title = request.POST['title']
        memo.content = request.POST['content']
        memo.save()
        messages.info(request, "Diary updated successfully.")
        return redirect("home")