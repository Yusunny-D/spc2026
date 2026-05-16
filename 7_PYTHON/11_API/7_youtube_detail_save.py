import os
from dotenv import load_dotenv
import requests
import csv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

main_video_url = 'https://www.googleapis.com/youtube/v3/videos'

video_ids = []

with open('search_result.csv', 'r', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        video_ids.append(row['video_id'])

params = {
    'part': "snippet, statistics",
    'id': ','.join(video_ids),
    'key': API_KEY
}

response = requests.get(main_video_url, params)
data = response.json()


table = []

# 가져오고 싶은 추가 정보
table_header = ['index', 'title', 'view count', 'like count', 'comment count']

with open("video_state.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(table_header)

    for item in data['items']:
        video_id = item['id']
        title = item['snippet']['title']
        state = item['statistics']
        view_count = state.get("ViewCount", 0)
        like_count = state.get("likeCount", 0)
        comment_count = state.get("commetCount", 0)

        writer.writerow([video_id, title, view_count, like_count, comment_count])
