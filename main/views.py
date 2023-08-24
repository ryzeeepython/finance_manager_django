from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm, DateForm, AddExpenseForm, SettingsForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserAccount, Expense
from .utils import Logic
import datetime
# Create your views here.

def index(request):
    if request.user.is_authenticated: 

        if request.method == 'POST':
            date_form = DateForm(request.POST)
            if date_form.is_valid():
                date = str(date_form.cleaned_data['date'])
                return render(request, 'main/main.html', Logic.get_expenses(user = request.user, date = date, form = date_form))
        else: 
            date_form = DateForm()
            if not(request.GET.get('time')): 
                today = datetime.datetime.now().date()
                request.session['date'] = str(today)

            if request.GET.get('time') == 'prev_day':
                date = datetime.datetime.strptime(request.session.get('date'), '%Y-%m-%d') 
                prev_date = date - datetime.timedelta(days=1)
                request.session['date'] = str(prev_date.date())

            if request.GET.get('time') == 'month':
                return render(request, 'main/main.html', Logic.get_expenses(user = request.user, date = 'МЕСЯЦ', form = date_form))

        return render(request, 'main/main.html', Logic.get_expenses(user = request.user, date = request.session.get('date'), form = date_form))
    else:   
        return render(request, 'main/index.html')



def add_expense(request):
    if request.method == 'POST':
        form = AddExpenseForm(request.POST)
        if form.is_valid():
            Logic.save_expense(form = form.cleaned_data, user = request.user)
            return render(request, 'main/add_expense.html', {'form': form, 'success': True})
    else: 
        form = AddExpenseForm()

    return render(request, 'main/add_expense.html', {'form': form, 'success': False})

@login_required()
def settings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            Logic.save_limits(user = request.user, data = form.cleaned_data)
            return render(request, 'main/settings.html', {'form': form, 'success': True})
    else:
        form = SettingsForm()
    return render(request, 'main/settings.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user_acc = UserAccount(user=user)
            user_acc.save()
            login(request, user)
            return redirect('/')
    else:
        user_form = RegisterUserForm()  


    return render(request, 'main/register.html', {'form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return render(request, 'main/login.html', {'form': form, 'access_denied': True})
    else:
        form = LoginUserForm()

    return render(request, 'main/login.html', {'form': form})   


def logout_user(request):
    logout(request)
    return redirect('/login')
