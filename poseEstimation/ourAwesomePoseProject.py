import cv2
import mediapipe as mp
import poseModule as pm
import time


cap = cv2.VideoCapture('media/1.mp4')
pTime = 0
detector = pm.poseDetector()

while True:
    success, img = cap.read()
    detector.findPose(img)
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (255, 0, 0), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
    (255, 0, 0),3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)


# if __name__ == "__main__":
#     main()