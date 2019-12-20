import cv2
from matplotlib import pyplot as plt

file="640-480.jfif"
color="gray"
bins=256

if color == 'rgb':
    img = cv2.imread(file) 
    plt.figure()
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[bins],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,bins-1])
        plt.title('Histogram (RGB)')
else:
    cap = cv2.imread(file, 0) 
    # bottom colored
    plt.hist(cap.ravel(),bins,[0,256])
    plt.title('Histogram (RGB)')
plt.xlabel("Bin")
plt.ylabel("Frequency")
plt.show()


