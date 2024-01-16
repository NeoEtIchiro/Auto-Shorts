from moviepy.editor import *
import random
import os
import cv2

dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def GetDaySuffix(day):
    if day == 1 or day == 21 or day == 31:
        return "st"
    elif day == 2 or day == 22:
        return "nd"
    elif day == 3 or day == 23:
        return "rd"
    else:
        return "th"

dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
music_path = os.path.join(dir_path, "Music/")

def add_return_comment(comment):
    need_return = 30
    new_comment = ""
    return_added = 0
    return_added += comment.count('\n')
    for i, letter in enumerate(comment):
        if i > need_return and letter == " ":
            letter = "\n"
            need_return += 30
            return_added += 1
        new_comment += letter
    return new_comment, return_added
        

class CreateMovie():

    @classmethod
    def CreateMP4(cls, post_data):
        background = VideoFileClip('C:\\Users\\neoet\\Desktop\\Programme\\Python\\AutoShorts\\AutoShortV2\\parkourPetit.mp4')

        r = random.randint(0, 330)
        background = background.subclip(r, r+15)
        image = ImageClip(post_data[0]['image_path']).set_start(0).set_duration(15).set_pos(("center", 30)).resize(width=640) # if you need to resize...
        
        clip = CompositeVideoClip([background, image])
        
        music_file = os.path.join(music_path, f"C:\\Users\\neoet\\Desktop\\Programme\\Python\\AutoShorts\\AutoShortV2\\Music\\music{random.randint(0,4)}.mp3")
        music = AudioFileClip(music_file)
        music = music.set_start((0,0))
        music = music.volumex(.4)
        music = music.set_duration(15)
        clip.audio = music
        
        clip.write_videofile("video.mp4", fps = 24)

if __name__ == '__main__':
    print(TextClip.list('color'))