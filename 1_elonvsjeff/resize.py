import cv2

name = './assets/lasedjeff.png'

new = cv2.imread(name)
new = cv2.resize(new, (64, 64))
cv2.imwrite('./assets/lasedjeff.png', new)