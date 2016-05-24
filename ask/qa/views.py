from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .forms import AskForm, AnswerForm, RegisterForm, LoginForm
from django.template.context import RequestContext
from .models import Question, Answer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User


def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_http_methods(['GET', 'HEAD'])
def index(request):
    page = request.GET.get('page')
    questions = Question.objects.order_by('-added_at')
    paginator = Paginator(questions, 10)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'page':page})

@require_http_methods(['GET', 'HEAD'])
def popular(request):
     page = request.GET.get('page')
     questions = Question.objects.order_by('-rating')
     paginator = Paginator(questions, 10)
     try:
         page = paginator.page(page)
     except PageNotAnInteger:
         page = paginator.page(1)
     except EmptyPage:
         page = paginator.page(paginator.num_pages)
     return render(request, 'popular.html', {'page':page})
                           
def question(request, id):
    try:
        question = Question.objects.get(pk=id)
    except:
        raise Http404
    answers = Answer.objects.filter(question=question)
    form = AnswerForm()
    return render(request, 'question.html', RequestContext(request, {'question':question, 'answers': answers, 'form':form}))

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', RequestContext(request, {'form': form}))

def answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'answer.html', RequestContext(request, {'form': form}))
    
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            username = form['username'].value()
            password = form['password'].value()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    django_login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', RequestContext(request, {'form': form}))

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', RequestContext(request, {'form': form}))

