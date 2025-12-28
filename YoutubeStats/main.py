from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import re 


load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
MAX_VIDEOS = 5  


youtube = build("youtube", "v3", developerKey=API_KEY)


def clean_title(title):

    cleaned = re.sub(r'[^a-zA-Z0-9]', ' ', title)

    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned


def main():
    search_input = input("Enter your YouTube Search Query: ")


    videos = search_youtube(search_input, max_total=MAX_VIDEOS)
    print(f"Found {len(videos)} videos. Fetching statistics...")


    videoIDs = [v["videoID"] for v in videos]


    stat_results = get_stats(videoIDs)


    for i, stat in enumerate(stat_results):
        videos[i]["Upload date"] = stat["snippet"]["publishedAt"]
        videos[i]["views"] = stat["statistics"].get("viewCount", 0)
        videos[i]["likes"] = stat["statistics"].get("likeCount", 0)
        videos[i]["videoTitle"] = clean_title(videos[i]["videoTitle"]).lower()
        videos[i]["Video tokens"] = videos[i]["videoTitle"].split()

 
    for video in videos:
        print(video)
        print()


def search_youtube(search_input, max_total=200):
    videos = []
    next_page_token = None

    while len(videos) < max_total:
        request = youtube.search().list(
            part="snippet",
            q=search_input,
            type="video",
            maxResults=50, 
            pageToken=next_page_token
        )
        results = request.execute()

        for item in results.get("items", []):
            videos.append({
                "videoID": item["id"]["videoId"],
                "videoTitle": item["snippet"]["title"]
            })

 
        next_page_token = results.get("nextPageToken")
        if not next_page_token:
            break

    return videos[:max_total]


def get_stats(videoIDs):
    stats = []

    for i in range(0, len(videoIDs), 50):  
        batch_ids = videoIDs[i:i+50]
        stat_request = youtube.videos().list(
            part="statistics, snippet",
            id=",".join(batch_ids)
        )
        stat_results = stat_request.execute()
        stats.extend(stat_results.get("items", []))

    return stats


if __name__ == "__main__":
    main()
