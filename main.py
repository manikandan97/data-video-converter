import io
from PIL import Image, ImageDraw
import cv2
import random

def generate_image(color):
    img = Image.new(mode = "1", size = (512, 512), color="white")
    draw = ImageDraw.Draw(img)
    for x in range(512):
        draw.point(xy = (random.randint(0,512), random.randint(0,512)), fill = "black")

    img.save(fp = "test.png")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

def generate_video():
    video_name = 'mygeneratedvideo.avi'

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'MJPG'), 60.0, (512, 512))
    
    for color in range(6):
        if (color == 1):
            for x in range(60):
                generate_image("black")
                image = cv2.imread("test.png")
                video.write(image)
        if (color == 2):
            for x in range(60):
                generate_image("yellow")
                image = cv2.imread("test.png")
                video.write(image)        
        if (color == 3):
            for x in range(60):
                generate_image("green")
                image = cv2.imread("test.png")
                video.write(image)      
        if (color == 4):
            for x in range(60):
                generate_image("blue")
                image = cv2.imread("test.png")
                video.write(image)   
        if (color == 5):
            for x in range(60):
                generate_image("red")
                image = cv2.imread("test.png")
                video.write(image)

    cv2.destroyAllWindows() 
    video.release()

generate_video()