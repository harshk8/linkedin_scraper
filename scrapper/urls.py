from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from scrapper import views

urlpatterns = [
    path('scrapper/', views.ScrapCompanyInfo.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)