import googleapiclient.discovery
import googleapiclient.errors
import json

API_KEY = ''

def generate_video_url(video_id: str, channel_name: str):
    yt_video_url = f"https://www.youtube.com/watch?v={video_id}&ab_channel={channel_name}"
    return yt_video_url

def main():
    api_service_name = "youtube"
    api_version = "v3"

    # Get credentials and create an API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    request = youtube.search().list(
        part="snippet",
        q="reutilizar agua al lavar ropa",
        maxResults=3
    )
    response = request.execute()
    # data = json.dumps(response)
    
    for i in range(len(response["items"])):
        video_id = response["items"][i]["id"]["videoId"]
        channel_name = response["items"][i]["snippet"]["channelTitle"]
        vid_url = generate_video_url(video_id, channel_name)
        print(f"Here's the url of the video {vid_url}")


main()
