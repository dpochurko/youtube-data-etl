from googleapiclient.discovery import build
import pandas as pd
from sqlalchemy import create_engine
import datetime

api_key = 'AIzaSyCxaa4Eumxbhfxoplk2H9___FcwwDSWkKc'
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    regionCode="US",
    maxResults=50
)
response = request.execute()

# Parse and normalize response
videos = []
for item in response['items']:
    videos.append({
        "video_id": item['id'],
        "title": item['snippet']['title'],
        "published_at": item['snippet']['publishedAt'],
        "views": int(item['statistics'].get('viewCount', 0)),
        "likes": int(item['statistics'].get('likeCount', 0)),
        "like_ratio": round(int(item['statistics'].get('likeCount', 0)) / max(int(item['statistics'].get('viewCount', 1)), 1), 4)
    })

df = pd.DataFrame(videos)

# PostgreSQL connection
# PostgreSQL connection
engine = create_engine("postgresql://postgres:password1@localhost:5432/youtube_data")

# Load into PostgreSQL
df.to_sql("trending_videos", engine, if_exists='append', index=False)

print("✅ Data inserted successfully.")
