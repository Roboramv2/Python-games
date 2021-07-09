import cv2

name = './assets/desboss.png'

new = cv2.imread(name)
new = cv2.resize(new, (64, 64))
cv2.imwrite('./assets/desboss.png', new)