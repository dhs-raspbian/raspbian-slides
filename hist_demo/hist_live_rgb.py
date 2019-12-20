import cv2
from matplotlib import pyplot as plt
import numpy as np

color='rgb'
bins=256
cap = cv2.VideoCapture(0)

# Initialize plot.
fig, ax = plt.subplots()
if color == 'rgb':
    ax.set_title('Histogram (RGB)')
else:
    ax.set_title('Histogram (grayscale)')
ax.set_xlabel('Bin')
ax.set_ylabel('Frequency')

 # Initialize plot line object(s). Turn on interactive plotting and show plot.
lw = 0.8
alpha = 0.7
if color == 'rgb':
    lineR, = ax.plot(np.arange(bins), np.zeros((bins,)), c='b', lw=lw, alpha=alpha)
    lineG, = ax.plot(np.arange(bins), np.zeros((bins,)), c='g', lw=lw, alpha=alpha)
    lineB, = ax.plot(np.arange(bins), np.zeros((bins,)), c='r', lw=lw, alpha=alpha)
else:
    lineGray, = ax.plot(np.arange(bins), np.zeros((bins,1)), c='k', lw=lw)
ax.set_xlim([0, bins-1])
ax.set_ylim([0, 8000])
plt.ion()
plt.show()

 # Grab, process, and display video frames. Update plot line object(s).
while True:
    (grabbed, frame) = cap.read()
    if not grabbed:
        break

    # Normalize histograms based on number of pixels per frame.
    numPixels = np.prod(frame.shape[:2])
    if color == 'rgb':
        cv2.imshow('RGB', frame)
        '''
        plt.figure()
        for i,col in enumerate(color):
            histr = cv2.calcHist([frame],[i],None,[256],[0,256])
            plt.plot(histr,color = col)
            plt.xlim([0,256])
        '''
        (b, g, r) = cv2.split(frame)
        histogramR = cv2.calcHist([r], [0], None, [bins], [0, 255])# / numPixels
        histogramG = cv2.calcHist([g], [0], None, [bins], [0, 255])# / numPixels
        histogramB = cv2.calcHist([b], [0], None, [bins], [0, 255])# / numPixels
        lineR.set_ydata(histogramR)
        lineG.set_ydata(histogramG)
        lineB.set_ydata(histogramB)
    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale', gray)
        histogram = cv2.calcHist([gray], [0], None, [bins], [0, 255]) / numPixels
        lineGray.set_ydata(histogram)
    fig.canvas.draw()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
plt.close()
