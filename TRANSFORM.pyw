from moviepy.editor import *

def convert(video, x, name):
    #Interpreting video
    clip = VideoFileClip(video)

    #getting only x seconds of video
    clip = clip.subclip(0,x)

    #save the gif
    clip.write_gif(name,".gif")

    return 


""" MAIN """

bannertext = """  __  __   __        __   __   __      
 /|  /  | /  | /| | /    /  | /  | /|/|
( | (___|(___|( | |(___ (   |(___|( / |
  | |\   |   )| | )    )|   )|\   |   )
  | | \  |  / | |/  __/ |__/ | \  |  / 
  
  """
print(bannertext)


file = input("Drag your file here and press enter : ")
second = int(input("How many second(s) should be your gif : "))
name = input("The name of the GIF : ")

convert(file, second, name)
