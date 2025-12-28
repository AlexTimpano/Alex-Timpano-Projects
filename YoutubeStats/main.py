from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import re 

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
MAX_VIDEOS = 5   # Maximum number of videos to fetch

# Initialize YouTube API client
youtube = build("youtube", "v3", developerKey=API_KEY)

#  Clean video titles
def clean_title(title):
    # Keep only letters, numbers, replace others with space
    cleaned = re.sub(r'[^a-zA-Z0-9]', ' ', title)
    # Collapse multiple spaces into one
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

#  Main program 
def main():
    search_input = input("Enter your YouTube Search Query: ")

    # Step 1: Search videos
    videos = search_youtube(search_input, max_total=MAX_VIDEOS)
    print(f"Found {len(videos)} videos. Fetching statistics...")

    # Step 2: Extract video IDs
    videoIDs = [v["videoID"] for v in videos]

    # Step 3: Get statistics for videos
    stat_results = get_stats(videoIDs)

    # Step 4: Add stats and cleaned titles to video dict
    for i, stat in enumerate(stat_results):
        videos[i]["Upload date"] = stat["snippet"]["publishedAt"]
        videos[i]["views"] = stat["statistics"].get("viewCount", 0)
        videos[i]["likes"] = stat["statistics"].get("likeCount", 0)
        videos[i]["videoTitle"] = clean_title(videos[i]["videoTitle"]).lower()
        videos[i]["Video tokens"] = videos[i]["videoTitle"].split()

    # Step 5: Print results
    for video in videos:
        print(video)
        print()

# Search function with pagination to exceed individual search limit
def search_youtube(search_input, max_total=200):
    videos = []
    next_page_token = None

    while len(videos) < max_total:
        request = youtube.search().list(
            part="snippet",
            q=search_input,
            type="video",
            maxResults=50,  # max allowed per page
            pageToken=next_page_token
        )
        results = request.execute()

        # Add video info to list
        for item in results.get("items", []):
            videos.append({
                "videoID": item["id"]["videoId"],
                "videoTitle": item["snippet"]["title"]
            })

        # Stop if no more pages
        next_page_token = results.get("nextPageToken")
        if not next_page_token:
            break

    return videos[:max_total]

#  Get video statistics in batches 
def get_stats(videoIDs):
    stats = []

    for i in range(0, len(videoIDs), 50):  # batch of 50
        batch_ids = videoIDs[i:i+50]
        stat_request = youtube.videos().list(
            part="statistics, snippet",  # include snippet for upload date
            id=",".join(batch_ids)
        )
        stat_results = stat_request.execute()
        stats.extend(stat_results.get("items", []))

    return stats

# Entry point 
if __name__ == "__main__":
    main()
