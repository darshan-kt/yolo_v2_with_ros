#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Webcam:

    def __init__(self):
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(0)
        self.image_pub = rospy.Publisher("camera/image_raw", Image, queue_size=1)
        self.rate = rospy.Rate(30)

    def capture_loop(self):
        while not rospy.is_shutdown():
            ret, frame = self.cap.read()

            if not ret:
                rospy.logerr("Failed to capture frame")
                continue

            image_message = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.image_pub.publish(image_message)

            self.rate.sleep()

    def shutdown(self):
        self.cap.release()

if __name__ == '__main__':
    try:
        rospy.init_node('webcam', anonymous=True)
        webcam = Webcam()
        webcam.capture_loop()
    except rospy.ROSInterruptException:
        pass
    finally:
        webcam.shutdown()