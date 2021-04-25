from picamera import PiCamera
from time import sleep
import upload_test

camera = PiCamera()

camera.start_preview()
sleep(1)
camera.capture('/usr/local/share/captures/image.jpg')
camera.stop_preview()
# sleep(3)

upload_test.upload_blob_filename('wm_timedata', '/usr/local/share/captures/image.jpg', 'time_image.jpg')

