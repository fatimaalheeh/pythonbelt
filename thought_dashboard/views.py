from django.shortcuts import render, redirect, HttpResponse
from . import models

import re

#validtion
def validate_text(text, min_length=2):
    verified = True
    if not text:
        verified = False
    elif len(text) < min_length:
        verified = False
    return verified

#regex
def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        if not models.is_duplicate_email(email):
            return True
    return False



def register(request):
    if request.method == "POST":
        if request.POST['login_type']=="register":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            confirm = request.POST['confirm']
            print(request.POST)
            if validate_text(first_name) and validate_text(last_name) and validate_text(password, min_length=8) and validate_email(email) and password == confirm:
                user = models.insert_new_user(first_name, last_name, email, password)
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = first_name
                    request.session['last_name'] = last_name
                return redirect('/dashboard')
        return redirect('/')
    return redirect('/')


def dashboard(request):
    if 'user_id' in request.session:
        thoughts = {}
        all_thoughts = models.get_all_thoughts()
        for thought in all_thoughts:
            thoughts[thought.id] = {'thought': thought, 'likes': models.get_likes(thought.like_count)}
        context = {
            "first_name": request.session['first_name'],
            "last_name": request.session['last_name'],
            "thoughts": thoughts
        }
        print(thoughts)
        return render(request, "dashboard.html", context)
    return redirect('/')


def login(request):
    if request.method == "POST":
        if request.POST['login_type']=="login":
            email = request.POST['email']
            passwd = request.POST['password']
            user = models.get_user(email, passwd)
            print(user)
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                return redirect('/dashboard')
        return redirect('/')
    return redirect('/')


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['first_name']
        del request.session['last_name']
    return redirect('/')


def reg_or_login(request):
    if "user_id" in request.session:
        return redirect("/dashboard")
    return render(request, "index.html")


def add_thought(request):
    if request.method == "POST":
        post_data = request.POST['thought']
        thought = models.insert_thought(request.session['user_id'], post_data)
    return redirect('/dashboard')


def add_likes(request, id):
    if request.method == "POST":
        post_data = request.POST['likes']
        like = models.insert_like(request.session['user_id'], post_data, id)
    return redirect('/dashboard')
