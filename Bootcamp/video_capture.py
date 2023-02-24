import cv2

vid = cv2.VideoCapture(0)

result = True
while result:
    ret, frame = vid.read()
    cv2.imwrite("test.jpg", frame)

    result = False
    print("Image Captured ...")

vid.release()

