from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path("", views.about_company, name="about_company"),
    path("<int:company_id>/", views.detail_company, name="detail_company"),
]