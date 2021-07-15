import cv2 as cv

# def changeRes(width,height):
#     # Live video
#     capture.set(3,width)
#     capture.set(4,height)


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# img = cv.imread('.\Resources\Photos\cat_large.jpg')
# cv.imshow('Cat', img)
# img_resized = rescaleFrame(img, scale=.3)
# cv.imshow('Cat Resized', img_resized)
# cv.waitKey(0)


# # Reading Videos
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.4)
    
    cv.imshow('Video Resized', frame_resized)
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
