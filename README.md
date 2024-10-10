[Routes]
1. Class Tweets(APIView)
- GET /api/v1/tweets: See all tweets[x]
- POST /api/v1/tweets: Create a tweet[x]

2. class TweetDetail(APIView)
- GET /api/v1/tweets/<int:pk>: See a tweet[x]
- PUT /api/v1/tweets/<int:pk>: Edit a tweet[x]
- DELETE /api/v1/tweets/<int:pk>: Delete a tweet[x]

3. class Users(APIView)
- GET /api/v1/users: See all users[x]
- POST /api/v1/users: Create a user account with password[x]

4. class UserDetail(APIView)
- GET /api/v1/users/<int:pk>: See user profile[x]

5. class UserTweet(APIView)
- GET /api/v1/users/<int:pk>/tweets: See tweets by a user[x]

6. class ChangePassword
- PUT /api/v1/users/password: Change password of logged in user.[x]

7. class Login(APIView) in users app
- POST /api/v1/users/login: Log user in[x]

8. class Logout(APIView) in users app
- POST /api/v1/users/logout: Log user out[x]


[Authentication]
- UsernameAuthentication라는 이름의 authentication class를 빌드하세요.[x]
- UsernameAuthentication 는 반드시 BaseAuthentication에서 extend 되어야 합니다.[x]
- X-USERNAME 헤더를 사용하는 유저를 찾으세요.[x]


[Testing]
- /api/v1/tweets: Test GET and POST methods[x]
- /api/v1/tweets/<int:pk>: Test GET, PUT and DELETE methods[x]