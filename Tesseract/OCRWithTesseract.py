# import the necessary packages
import cv2
import pytesseract


def readImage(pathname: str):
    """
    This method reading an image using cv2 and convert it to gray picture  
    Arguments:
        pathname (str): path to image

    Returns:
        Type: Mat
        Value: An image witt gray color

    """
    image = cv2.imread(pathname)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def preprocessing(img, preprocess: str = "thresh"):
    """
    This method using to preprocess image before Recongnition
    Arguments:
        img (Mat): Image need preprocess have been converted
        preprocess (str): Type of preprocess you want to
            Deffault: "thresh"
    Returns:
        Type: Mat
        Value: Image after preprocess
    """

    # If using Thresh or converted to black and white picture
    if preprocess == "thresh":
        return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # If using Blur the image to reduce noise
    elif preprocess == "blur":
        return cv2.medianBlur(img, 3)

    return img


def imgaeToString(pathname: str, preprocess="thresh", lang: str = "vie") -> str:
    """
    This method using to recongnition text in text
    Arguments:
        pathname (str): Path to image need to recongnition
        preprocess (str): Type of preprocess you want to
            Deffault: "thresh"
        lang (str): Language in the image
            Deffault: vie
    Returns:
        Type: str
        Value: Text in image
    """

    # Read image
    img = readImage(pathname)

    # Preprocess
    grayImg = preprocessing(img, preprocess)


    # Show image after preprocess
    cv2.imshow("After Preprocess", grayImg)

    # Using Tesseract
    return pytesseract.image_to_string(grayImg, lang=lang)

if __name__ == "__main__":

    # Path to image
    filename = "Image\\Example.jpg"
    
    # Type of preprocess
    preprocess = "thresh"
    
    # print output
    print(imgaeToString(filename, preprocess, "vie"))

    # Wait push any key
    cv2.waitKey(0)
