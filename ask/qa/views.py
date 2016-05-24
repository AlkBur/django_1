from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from qa.forms import AskForm, AnswerForm, RegisterForm, LoginForm

def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_http_methods(['GET', 'HEAD'])
def index(request, *args, **kwargs):
    page = request.GET.get('page')
    return render(request, 'index.html', {'page':page})

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

