from django.urls import path
from todo import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('task_list/',views.TaskList.as_view(),name='task_list'),
    path('add_task/',views.AddTask.as_view(),name='add_task'),
    path('update_task/<str:pk>/',views.UpdateTask.as_view(),name='update_task'),
    path('delete_task/<str:pk>/',views.DeleteTask.as_view(),name='delete_task'),
    path('sign_up/',views.SignUp.as_view(),name='sign_up'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
