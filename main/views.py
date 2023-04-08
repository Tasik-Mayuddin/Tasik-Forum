from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Thread, Profile, Post
from register.forms import PictureForm
from django.contrib.auth.models import User


# Create your views here.
def home(response):
    ls = Thread.objects.all()

    if response.method == 'POST':

        if response.POST.get("save"):

            txt = response.POST.get("new")
            txt2 = response.user
            t = Thread.objects.create(name=txt,user=txt2)
            return HttpResponseRedirect("/threads/%i" %t.id)

        elif response.POST.get("sort-number"):
            ls = ls.order_by("-post_count")
        elif response.POST.get("sort-created"):
            ls = ls.order_by("-created_at")
        elif response.POST.get("sort-last"):
            ls = ls.order_by("-edited_at")

        return render(response, 'main/home.html',{"ls":ls})

    else:

        return render(response, 'main/home.html',{"ls":ls,"current_user":response.user})

def index(response,id):

    cont = Thread.objects.get(id=id)
    current_user = response.user

    if response.method == 'POST':

        if response.POST.get("post-submit"):
            
            txt = response.POST.get("frm-post")
            cont.post_set.create(content=txt, user=current_user)
            cont.post_count = cont.post_set.all().count()
            cont.save()
            return HttpResponseRedirect("/threads/%i" %id)

        elif response.POST.get("delpos"):

            rel = response.POST.get("delpos")

            if current_user == cont.post_set.get(id=rel).user:

                cont.post_set.get(id=rel).delete()
                cont.post_count = cont.post_set.all().count()
                cont.save()

            return HttpResponseRedirect("/threads/%i" %id)

        elif response.POST.get("delthr") and current_user==cont.user:

            cont.delete()
            return redirect("/")

        elif response.POST.get("reply-submit"):

            txt = response.POST.get("frm-reply")
            txt2 = response.POST.get('reply-submit')
            cont.post_set.create(content=txt, user=current_user, reply=txt2)
            cont.post_count = cont.post_set.all().count()
            cont.save()
            return HttpResponseRedirect("/threads/%i" %id)

        elif response.POST.get("edit-submit"):

            rel = response.POST.get("edit-submit")

            if current_user == cont.post_set.get(id=rel).user:
           
                txt = response.POST.get("frm-edit")
                t = cont.post_set.get(id=rel)
                t.content = txt
                t.edit_status = True
                t.save()
                cont.save()

            return HttpResponseRedirect("/threads/%i" %id)

        else:

            return HttpResponseRedirect("/threads/%i" %id)

    else:

        return render(response, 'main/thread.html', {"cont":cont,"current_user":current_user,"user_inst":User})

def profile(response):

    current_user = response.user
   
    if response.method == 'POST':

        form = PictureForm(response.POST, response.FILES, instance=current_user.profile)

        if form.is_valid():

            form.save()
            return redirect("/profile")

    else:

        form = PictureForm()

    return render(response,'main/profile.html',{"current_user":current_user, "form":form})


def userposts(response,uname):
    
    rel_user = User.objects.get(username=uname)
    post_list = Post.objects.filter(user=rel_user)

    return render(response, 'main/userposts.html', {"current_user":rel_user,"post_list":post_list})

def search(response,word):
    current_user = response.user
    word = word.split()
    t_obj = Thread.objects
    p_obj = Post.objects
    ls = []
            
    for x in word:
        add_pool1 = t_obj.filter(name__icontains=x)
        add_pool2 = p_obj.filter(content__icontains=x)
        for y in add_pool1:
            if y not in ls:
                ls.append(y)
        for y in add_pool2:
            if y.thread not in ls:
                ls.append(y.thread)

    if response.method == "POST":
            
        if response.POST.get("sort-number"):
            ls = sorted(ls, key=lambda x: x.post_count, reverse=True)
        elif response.POST.get("sort-created"):
            ls = sorted(ls, key=lambda x: x.created_at, reverse=True)
        elif response.POST.get("sort-last"):
            ls = sorted(ls, key=lambda x: x.edited_at, reverse=True)

    return render(response, 'main/search.html', {"current_user":current_user,"ls":ls})
    

############effeciency functions

def search_eff(txt):
    txt = txt.split()
    t_obj = Thread.objects
    p_obj = Post.objects
    pool = []

    for x in txt:
        add_pool1 = t_obj.filter(name__icontains=x)
        add_pool2 = p_obj.filter(content__icontains=x)
        for y in add_pool1:
            if y not in pool:
                pool.append(y)
        for y in add_pool2:
            if y.thread not in pool:
                pool.append(y.thread)
    return pool