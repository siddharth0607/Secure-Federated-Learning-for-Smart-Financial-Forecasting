from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'landing_page.html')

def export_reports(request):
    return render(request, 'Fraud_Alerts/fraud_index.html')

def fraud_alerts(request):
    return render(request, 'Fraud_Alerts/fraud_index.html')

@login_required
def track_expenses(request):
    return render(request, 'Expense_Tracker/base.html')  # This can be adjusted later to render a dedicated dashboard


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate the user and log them in
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after login
            else:
                # Invalid login, re-render the login form with an error message
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
