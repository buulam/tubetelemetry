# tubetelemetry

```
pip install fastapi uvicorn httpx dotenv google-auth google-auth-oauthlib
```

Create a .env file

```
VIEWS=https://youtubeanalytics.googleapis.com/v2/reports?endDate=2025-07-31&filters=video%3D%3DNG2_AE2_zOg&ids=channel%3D%3DMINE&metrics=views%2Ccomments%2Clikes%2Cdislikes%2CestimatedMinutesWatched%2CaverageViewDuration&startDate=2023-09-01
SCOPES=https://www.googleapis.com/auth/yt-analytics.readonly
VIDEO=
```