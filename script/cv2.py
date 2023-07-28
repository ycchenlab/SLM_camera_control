# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:28:07 2023

@author: ycche
"""

import cv2

def main():
    # Initialize the camera
    cap = cv2.VideoCapture(1)  # 0 for default camera, or specify the camera ID

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Perform signal analysis (e.g., image processing, computer vision) on the frame here

        # Display the frame
        cv2.imshow('Camera Feed', frame*5)

        # Exit the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()