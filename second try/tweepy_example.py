
import cv2 

import time 
import sys 
import imutils 
from PIL import Image 
import os


import tweepy 



consumer_key = 'cbaYof2MIyE78O0oYOl4aecc1'  
consumer_secret = 'bLJTCKVL7wDUVOLQIyHevDGjAfga1PVifcSGtryISoUHhuLkRG'
access_token = '1494408772227411972-MDHqUqKpNL0sMfbk3KcaGFQUfWH4ty'
access_token_secret = 'Id8p66fhBn4PxzIhe0fKPA02tZQcJTkk3D9D0ccWjpMQo'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

cam_port = 2 

video = cv2.VideoCapture('video.mp4') 
if (video.isOpened() == False):
  print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

result = cv2.VideoWriter('newVideo.mp4',
                         cv2.VideoWriter_fourcc('M','J','P','G'),
                         10, size)

while(video.isOpened()):

  res, frame = video.read()

  if res == True:

    result.write(frame)

    cv2.imshow('Frame', frame)
    cv2.imwrite('Frame.png', frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):

      statusMessage = "Hi I am an image!"
      api.update_status_with_media(statusMessage,"Frame.png") 
   
      break
  else:
      break

video.release()
result.release()

cv2.destroyAllWindows()

print("yay")
text = 'yay'
print(".. ", text)
