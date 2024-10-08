from django.urls import path
from . import views



urlpatterns = [
	path('', views.Tweets.as_view()),
    path('<int:tweet_pk>', views.TweetDetail.as_view()),
]