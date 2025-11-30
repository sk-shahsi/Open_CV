import cv2

video = cv2.VideoCapture(
    "E:/Personal/video/Songs/Bhojpuri/y2mate.com - video  Sajanwa  Khesari Lal Yadav  सजनव  FT Rani  Latest Bhojpuri Video Song 2023_1440p.mp4")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

output = cv2.VideoWriter("output.mp4", fourcc, 25.0, (1920, 1080))

while video.isOpened():
    ret,frame = video.read()
    if ret:
        output.write(frame)
        cv2.imshow("frame", frame)

        if cv2.waitKey(10)  == ord('s'):
            break

        else:
            break

cv2.destroyAllWindows()