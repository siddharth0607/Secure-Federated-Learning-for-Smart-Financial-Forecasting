from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import fraud_alerts_view, predict_fraud

urlpatterns = [
   path('', fraud_alerts_view, name='fraud_alerts'),  # Main fraud alerts page
    path('predict/', predict_fraud, name='fraud_predict'),  # Fraud prediction URL



]
