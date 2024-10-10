from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from tweets.models import Tweet
from users.models import User


class TestTweets(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="test_user")
        self.tweet = Tweet.objects.create(
            user=self.user,
            payload="test tweet"
        )
        self.tweets_url = reverse('tweets')
        self.tweet_detail_url = reverse('tweet_detail', args=[self.tweet.pk])
    
    def test_get_tweets(self):        
        response = self.client.get(self.tweets_url) #요청 > 응답
        self.assertEqual(response.status_code, status.HTTP_200_OK) #응답 확인

    def test_post_tweets(self):
        self.client.force_authenticate(user=self.user) #인증
        data = {"payload": "test post tweet"}
        response = self.client.post(self.tweets_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tweetDetail(self):
        self.client.force_authenticate(user=self.user) #인증
        response = self.client.get(self.tweet_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_tweetDetail(self):
        self.client.force_authenticate(user=self.user)
        update_data = {'payload': 'test put tweet'}
        response = self.client.put(self.tweet_detail_url, update_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_delete_tweetDetail(self):
        self.client.force_authenticate(user=self.user) #인증
        response = self.client.delete(self.tweet_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
