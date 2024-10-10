from django.urls import path
from . import views



urlpatterns = [
	path('', views.Tweets.as_view(), name="tweets"),
    path('<int:tweet_pk>', views.TweetDetail.as_view(), name="tweet_detail"),
]