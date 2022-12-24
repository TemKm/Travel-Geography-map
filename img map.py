import cv2
import numpy as np

img = cv2.imread('map/spain.jpg')                             # 이미지 불러오기
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                  # 이미지 그레이 전환

ret, thresh = cv2.threshold(imgray, 120, 255, 0)                                # 흑과 백으로 임계(threshold) 분할
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)     # contour(외곽선)를 찾아냄.(연속된 좌표점)

cv2.drawContours(img, contours , -1, (0, 255, 0), 2)                            # contour(외곽선)을 그림, 초록색(0 255 0), 두께 2로 -- 확인용
cv2.imshow('', img)                                                                 # 이미지 출력

contours = np.array(contours)
arr= contours.ravel()                                                          # N차원의 꼭지점 배열을 1차원으로 축소
print('--좌표--\n')
print(*arr, sep=',')                                                            # 배열사이에 들어갈 문자를 지정한 뒤 출력
print('\n')