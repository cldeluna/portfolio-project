from django.urls import path

from . import views

#Because the home page has the jobs screen the home page is in the jobs app
urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/',views.detail, name='detail'),

]
