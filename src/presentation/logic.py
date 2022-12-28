import cv2

def add_numbers(x: int, y: int) -> int:
    return x + y

def retrieveimage(image):
    i = cv2.imread(image, 0)
    return i
