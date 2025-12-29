from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import re 
import nltk
from nltk.corpus import stopwords
import numpy
import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter

#setup for youtube API
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
MAX_VIDEOS = 100

#Setup for cleaning
nltk.download('stopwords')
nltk.download('punkt')
stopwords = set(stopwords.words('english'))


youtube = build("youtube", "v3", developerKey=API_KEY)

#Cleans video titles, leaves only alphanumeric
def clean_title(title):
    cleaned = re.sub(r'[^a-zA-Z]', ' ', title)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned



def main():
    search_input = input("Enter your YouTube Search Query: ")


    videos = search_youtube(search_input, max_total=MAX_VIDEOS)
    print(f"Found {len(videos)} videos. Fetching statistics...")


    videoIDs = [v["videoID"] for v in videos]


    stat_results = get_stats(videoIDs)

    #Compiles statistical information into video info for final results
    for i, stat in enumerate(stat_results):
        videos[i]["Upload date"] = stat["snippet"]["publishedAt"][0:10]
        videos[i]["views"] = stat["statistics"].get("viewCount", 0)
        videos[i]["likes"] = stat["statistics"].get("likeCount", 0)
        videos[i]["videoTitle"] = clean_title(videos[i]["videoTitle"]).lower()
        videos[i]["Video tokens"] = videos[i]["videoTitle"].split()
        videos[i]["Video tokens"] = [token for token in videos[i]["Video tokens"] if (token not in stopwords and token !=search_input.lower())]
 
    videoDF = pd.DataFrame(videos)
    
    while True:
        print("\n=====What would you like to do with your data?=====")
        print("1: See a graphical breakdown of key words")
        print("2: Analyze whether videos with a certain key word in their titles see more views than those without")
        print("3: Exit")

        try:
            action = int(input("Enter your selection (1-3): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.\n")
            continue

        if action == 1:
            graph(videoDF)
        elif action == 2:
            word = input("Enter the keyword to analyze: ").strip().lower()
            with_views, without_views = word_views(videoDF, word)
            print(f"Average views for videos WITH '{word}': {with_views}")
            print(f"Average views for videos WITHOUT '{word}': {without_views}")
        elif action == 3:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.\n")




#Use youtube API with paginination to exceed individual search limits and collect  bulk youtube videos from query
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

        #Move to next page
        next_page_token = results.get("nextPageToken")
        if not next_page_token:
            break

    return videos[:max_total]

#Use video IDs to acquire deeper statistical information 
def get_stats(videoIDs):
    stats = []

    for i in range(0, len(videoIDs), 50):  #Get stats on 50 videos at a time 
        batch_ids = videoIDs[i:i+50]
        stat_request = youtube.videos().list(
            part="statistics, snippet",
            id=",".join(batch_ids)
        )
        stat_results = stat_request.execute()
        stats.extend(stat_results.get("items", []))

    return stats

def graph(dataframe):
    word_counts = count_words(dataframe['Video tokens'].tolist())
    # Take top 10 most frequent words
    top_ten = dict(list(word_counts.items())[:10])

    plt.bar(top_ten.keys(), top_ten.values())
    plt.xlabel("Keyword")
    plt.ylabel("Frequency")
    plt.title("Frequency of keywords in video titles")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()  # add parentheses

    plt.show()



def count_words(words_list_of_lists):
    flat_list = [token for sublist in words_list_of_lists for token in sublist]
    
    word_counts = Counter(flat_list)
    
    return dict(word_counts.most_common())

def word_views(dataframe, word="music"):
    with_word = dataframe[dataframe["Video tokens"].apply(lambda x: word in x)]
    without_word = dataframe[dataframe["Video tokens"].apply(lambda x: word not in x)]
    
    avg_with = with_word["views"].apply(int).median()

    if avg_with == 'nan':
        avg_with=0
    avg_without = without_word["views"].apply(int).median()
    if avg_without=='nan':
        avg_without=0
    
    return avg_with, avg_without


#Entry point
if __name__ == "__main__":
    main()