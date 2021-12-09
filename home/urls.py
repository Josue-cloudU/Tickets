from django.urls import path
from home import views
app_name = "home"
from home import views as views

urlpatterns = [
    path('pricing', views.Pricing.as_view(), name="Pricing"),
    path('rutas', views.Rutas.as_view(), name="Rutas"),
    path('ticket', views.Ticket.as_view(), name="Ticket"),
]
