import cv2

# Cascade
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read image, create grayscale version of it
img=cv2.imread("news.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Creates 'faces' numpy array
faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1, # Controls scaling slices that program looks at
minNeighbors=5)

# Draws rectangle around face
# Takes img, top-left corner, bottom-right corner, RBG value, line width
for x, y, w, h in faces:
    img=cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

print(type(faces))
print(faces)

# Scales down image in case it's too large for screen
resized=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# Shows image
cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()