"""

File: camera_test.py
 
This code will test Raspberry Pi Camera
"""

from picamera import PiCamera
from time import sleep

camera = PiCamera()


def main():
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
