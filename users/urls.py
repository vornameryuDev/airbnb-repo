from django.urls import path

from users import views


urlpatterns = [
 	path('', views.all_users),
	path('<int:user_pk>', views.user),
	path('<int:user_pk>/tweets/', views.user_tweets), 
]