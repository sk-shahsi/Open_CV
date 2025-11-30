import cv2

video = cv2.VideoCapture("E:/Personal/video/Songs/Bhojpuri/y2mate.com - video  Sajanwa  Khesari Lal Yadav  सजनव  FT Rani  Latest Bhojpuri Video Song 2023_1440p.mp4")
while(video.isOpened()):
    ret,frame = video.read()
    ret,frame = video.read()

    frame = cv2.resize(frame,(800,700))

    cv2.imshow('Output',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()