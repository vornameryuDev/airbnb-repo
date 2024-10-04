from django.urls import path

from users import views


urlpatterns = [
 	path('', views.Users.as_view()),
	path('<int:user_pk>', views.UserDetail.as_view()),
	path('<int:user_pk>/tweets/', views.UserTweets.as_view()), 
]