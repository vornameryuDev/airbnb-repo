[Routes]
1. Class Tweets(APIView)
- GET /api/v1/tweets: See all tweets
- POST /api/v1/tweets: Create a tweet

2. class TweetDetail(APIView)
- GET /api/v1/tweets/<int:pk>: See a tweet
- PUT /api/v1/tweets/<int:pk>: Edit a tweet
- DELETE /api/v1/tweets/<int:pk>: Delete a tweet

3. class Users(APIView)
- GET /api/v1/users: See all users
- POST /api/v1/users: Create a user account with password

4. class UserDetail(APIView)
- GET /api/v1/users/<int:pk>: See user profile

5. class UserTweet(APIView)
- GET /api/v1/users/<int:pk>/tweets: See tweets by a user

6.
- PUT /api/v1/users/password: Change password of logged in user.

7. class Login(APIView) in users app
- POST /api/v1/users/login: Log user in

8. class Logout(APIView) in users app
- POST /api/v1/users/logout: Log user out


[Authentication]
- UsernameAuthentication라는 이름의 authentication class를 빌드하세요.
- UsernameAuthentication 는 반드시 BaseAuthentication에서 extend 되어야 합니다.
- X-USERNAME 헤더를 사용하는 유저를 찾으세요.


[Testing]
- /api/v1/tweets: Test GET and POST methods
- /api/v1/tweets/<int:pk>: Test GET, PUT and DELETE methods