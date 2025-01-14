import cv2

image = cv2.resize(cv2.imread("image.png", cv2 .IMREAD_GRAYSCALE), (150,65))
charset = "@#&=(/~ "

for row in image:
    print()
    for pixel in row:
        new_value = round((pixel / 255) * (len(charset)-1))
        print(charset[7-new_value], end="")
