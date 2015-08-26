from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from models import Theme, Question, Answer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import FormView, View, UpdateView, DeleteView, BaseUpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from actions import test, question, answer


class Home(TemplateView):
    template_name = 'tests/base.html'


class ThemeView(ListView):
    template_name = 'tests/theme.html'
    models = Theme

    def get(self, request, *arg, **kwargs):
        theme = Theme.objects.all()
        return render(request, self.template_name, {'theme': theme})


class Login(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'tests/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(Login, self).form_valid(form)


class LogOut(View):
    success_url = '/login/'
    template_name = 'tests/base.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class TestsView(DetailView):
    model = Question
    template_name = 'tests/tests.html'
    # fields = ['name', ]

    # def get(self, request, *args, **kwargs):
    #     th = Theme.objects.get(id=kwargs['pk'])
    #     q = Question.objects.filter(theme=th)
    #     a = Answer.objects.all()
    #     for j in q:
    #         n = j.answer_set.all()
    #         print n
    #         for k in n:
    #             print k.answer
    #     return HttpResponse(k)
    def get_context_data(self, **kwargs):
        context = super(TestsView, self).get_context_data(**kwargs)
        context['question'] = question(**kwargs)
        context['answer'] = answer(**kwargs)

        return context
        # print context


def foo(request):
    print request.POST
    for key, value in request.POST.items():
        print key, value


    return HttpResponse('ok')
