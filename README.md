# tubetelemetry

```
pip install fastapi uvicorn httpx dotenv google-auth google-auth-oauthlib Requests
```

Create a .env file

```
VIEWS=https://youtubeanalytics.googleapis.com/v2/reports?endDate=2025-07-31&filters=video%3D%3DNG2_AE2_zOg&ids=channel%3D%3DMINE&metrics=views%2Ccomments%2Clikes%2Cdislikes%2CestimatedMinutesWatched%2CaverageViewDuration&startDate=2023-09-01
SCOPES=https://www.googleapis.com/auth/yt-analytics.readonly
VIDEO=this is where you put the video ID (appened on video URL's after v=)
```

Configuring OAuth took a bit of time. While this article doesn't step by step apply, it does teach you enough to be able to apply the elements towards this app.

[How to access Google APIs using OAuth in Postman](https://blog.postman.com/how-to-access-google-apis-using-oauth-in-postman/)