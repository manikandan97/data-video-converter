import io
from PIL import Image, ImageDraw
import cv2
import random
import logging
from time import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_image(color):
    img = Image.new(mode = "1", size = (128, 128), color="white")
    draw = ImageDraw.Draw(img)
    for x in range(128):
        for y in range(128):
            if (random.randint(0,1) == 1):
                draw.point(xy = (x,y), fill = "black")

    img.save(fp = "test.png")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

def generate_video():
    video_name = 'mygeneratedvideo.avi'

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'MJPG'), 60.0, (128, 128))
    
    for color in range(60):
        for x in range(60):
            generate_image("black")
            image = cv2.imread("test.png")
            video.write(image)

    cv2.destroyAllWindows() 
    video.release()

def main():
    ts = time()
    generate_video()
    logging.info('Took %s seconds', time() - ts)

if __name__ == '__main__':
    main()