from django.urls import path
from home import views
app_name = "home"
from home import views as views

urlpatterns = [
    path('pricing', views.Pricing.as_view(), name="Pricing"),
]
