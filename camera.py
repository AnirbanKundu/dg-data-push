import time
import picamera

with picamera.PiCamera() as camera:
    #camera.start_preview()
    time.sleep(0)
    camera.capture('dg.jpg')
    #camera.stop_preview()