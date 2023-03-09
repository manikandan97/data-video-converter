import io
from PIL import Image, ImageDraw
import cv2
import random
import logging
from time import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def open_file():
    in_file = open("text_file.txt", "rb") 
    data = in_file.read()
    byte_array = bytearray(data)
    res = []
    for byte in byte_array:
        binary_rep = bin(byte)
        res.append(binary_rep[2:])
    generate_image_using_data(res)    
    in_file.close()

def generate_image_using_data(data):
    img = Image.new(mode = "1", size = (512, 512), color="white")
    draw = ImageDraw.Draw(img)
    for x in range(len(data)):
        for y in range(len(data[x])):
            if (data[x][y] == '1'):
                draw.point(xy = (x,y), fill = "black")

    img.save(fp = "test.png")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()    

def generate_image():
    img = Image.new(mode = "1", size = (16, 16), color="white")
    draw = ImageDraw.Draw(img)
    for x in range(16):
        for y in range(16):
            if (random.randint(0,1) == 1):
                draw.point(xy = (x,y), fill = "black")

    img.save(fp = "test.png")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

def generate_video():
    video_name = 'mygeneratedvideo.avi'

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'MJPG'), 60.0, (16, 16))
    
    for color in range(1):
        for x in range(60):
            generate_image()
            image = cv2.imread("test.png")
            video.write(image)

    cv2.destroyAllWindows() 
    video.release()

def main():
    ts = time()
    #generate_video()
    logging.info('Took %s seconds', time() - ts)
    open_file()

if __name__ == '__main__':
    main()
    