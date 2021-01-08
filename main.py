import cv2


def cam_vision():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff = cv2.absdiff(frame1, frame2)  # Finding the difference of two frames
        gray = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)  # Turning difference of frames into only gray scale
        blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Making some Blur
        _, thresh = cv2.threshold (blur, 20, 255, cv2.THRESH_BINARY)  # Removing Unwanted Noise
        dilated = cv2.dilate(thresh, None, iterations=3)  # Increasing Scale
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Outline the all small movement
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)  # Drawing Green Outline on the frame

        # Looking for only large moving objects
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow('Security Cam', frame1)


if __name__ == '__main__':
    cam_vision()
