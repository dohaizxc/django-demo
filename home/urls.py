from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name = 'home'),
    path('course/<str:pk>', views.get_course),
    path('topic/<str:pk>', views.get_topic),
    path('create-course', views.create_course),
    path('update-course/<str:pk>', views.update_course),
    path('delete-course/<str:pk>', views.delete_course),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('bar-chart/', views.bar_chart, name='bar-chart'),
    path('get-bar-chart/', views.get_bar_chart, name='get-bar-chart'),
    path('admin-login', views.admin_login, name = 'admin-login'),
    path('logout/', views.logout_view, name='logout'),
]