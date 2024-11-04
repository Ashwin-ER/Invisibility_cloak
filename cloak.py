import cv2
import numpy as np
cam = cv2.VideoCapture(0)

for i in range(30):
    status, background = cam.read()
background = np.flip(background, axis=1)
print("Background Captured...")

round = cam.read()
while cam.isOpened():
    return_val, img = cam.read()
    if not return_val:
        break
    img = np.flip(img, axis=1)
    # convert color in BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # taking upper and lower range for hsv color
    lower_green = np.array([25, 52, 72])
    upper_green = np.array([102, 255, 255])

    lower_green = np.array([50, 80, 50])
    upper_green = np.array([90, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    # Refining the mask to tune green color
    # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))  # close_mask
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))  # open_mask
    # mask = cv2.dilate(mask, np.ones((10, 10), np.uint8), iterations=1)  # dilation
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

    cloth = cv2.bitwise_and(background, background, mask=mask)
    inverse_mask = cv2.bitwise_not(mask)

    # # final Output
    current = cv2.bitwise_and(img, img, mask=inverse_mask)
    combined = cv2.add(cloth, current)
    cv2.imshow("magic Happens Here", combined)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break