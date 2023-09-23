
from django.contrib import admin
from django.urls import path
from aptitude_test import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome_page, name='welcome_page'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('quiz/submit/', views.quiz_submit, name='quiz_submit'),
    path('thank-you/<int:total_score>/', views.thank_you_page, name='thank_you_page')

]

 