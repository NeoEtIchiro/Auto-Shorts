from datetime import date
import time
from CreateMovie import CreateMovie, GetDaySuffix
from RedditBot import RedditBot
from upload_video import upload_video
import moviepy.editor as mp

redditbot = RedditBot()
a = True

# clip = mp.VideoFileClip("AutoShorts\\AutoShortV2\\parkour.mp4")
# clip_resized = clip.resize(newsize=(720,1080))
# clip_resized.write_videofile("AutoShorts\\AutoShortV2\\parkourPetit.mp4")

while a:

    # Gets our new posts pass if image related subs. Default is memes
    post = redditbot.get_posts("dankmemes")
    
    # Create folder if it doesn't exist
    redditbot.create_data_folder()
    
    redditbot.save_image(post[0])
    
    CreateMovie.CreateMP4(redditbot.post_data)
    
    video_data = {
            "file": "video.mp4",
            "title": f"{redditbot.post_data[0]['title']} - Dankest memes !",
            "description": "#shorts\nGiving you the hottest memes of the day !",
            "keywords":"meme,reddit,Dankestmemes",
            "privacyStatus":"public"
    }

    print(video_data["title"])
    print("Posting Video ...")
    upload_video(video_data)
    
    a = False