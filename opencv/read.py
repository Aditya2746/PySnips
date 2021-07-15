import cv2 as cv

# Reading Image

# img = cv.imread('.\Resources\Photos\cat.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)

# Reading Video

vid = cv.VideoCapture('.\Resources\Videos\dog.mp4') # for webcamera or any attached camera to Computer pass integer

while True:
    isTrue, frame = vid.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

vid.release()
cv.destroyAllWindows()


