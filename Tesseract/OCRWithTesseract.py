# import the necessary packages
from PIL import Image
import pytesseract
import cv2

def readFile(pathname: str):
    # Đọc file ảnh và chuyển về ảnh xám
    image = cv2.imread(filename)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def preprocessing(img, preprocess: str = "thresh"):
    # Check xem có sử dụng tiền xử lý ảnh không

    # Nếu phân tách đen trắng
    if preprocess == "thresh":
        return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Nếu làm mờ ảnh
    elif preprocess == "blur":
        return cv2.medianBlur(img, 3)

    return img


def imgaeToString(pathname: str, preprocess="thresh", lang: str = "vie") -> str:
    img = readFile(pathname)
    grayImg = preprocessing(img, preprocess)
    cv2.imshow("Output", grayImg)

    # Load ảnh và apply nhận dạng bằng Tesseract OCR
    return pytesseract.image_to_string(grayImg, lang=lang)



"""
Hướng dẫn sử dụng module tesseract xem tại: https://www.youtube.com/watch?v=6DjFscX4I_c

* Xây dựng hệ thống tham số đầu vào
 - filename: Đường dẫn tới file ảnh cần nhận dạng
 - preprocess: tham số tiền xử lý ảnh (có thể bỏ qua nếu không cần)
    + blur : Làm mờ ảnh để giảm noise
    + thresh: Phân tách đen trắng"""
if __name__ == "__main__":

    filename = "Test1.jpg"
    preprocess = "thresh"

    # In dòng chữ nhận dạng được
    print(imgaeToString(filename, preprocess, "vie"))

    # Đợi chúng ta gõ phím bất kỳ
    cv2.waitKey(0)
