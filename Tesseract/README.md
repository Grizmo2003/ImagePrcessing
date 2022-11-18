# **USING THE TESSERACT MODULE FOR OPTICAL CHARACTER RECOGNITION**

## 1 What is Tesseract module ?
Tesseract OCR provides an OCR tool – libtesseract and a command line program – tesseract. Compared to the Tesseract 3 version, Tesseract 4 adds an OCR engine based on artificial neural networks (LSTMs), focusing on line recognition and character patterns. Tesseract supports many output formats such as text, hOCR (HTML), PDF, TSV, as well as experimental ALTO (XML) output.

You can read about data set [Here](https://www.libhunt.com/r/tesseract)

## 2 How to use Tesseract module ?
### 2.1 Install Tesseract

### MacOS:
We will install using the Homebrew tool. You type the following command:

```brew install tesseract```

After typing, you wait to run the command to finish.

![MAC OS](Image\tesseract_install_macos.jpg)

Source: pyimagesearch

### Linux: 
You use apt-get as follows:

```sudo apt-get install tesseract-ocr```

Then sit back and wait for it to run out of commands.

![Linux](Image\tesseract_install_ubuntu.jpg)

Source: pyimagesearch

### Window:
You download the installation file [Here](https://github.com/UB-Mannheim/tesseract/wiki) (remember to choose the 32 bit and 64 bit versions suitable for your window).

![Window](Image\tesseract_install_window.jpg)

### 2.2 Set up envirroment

Default language does not have Vietnamese, so you need to dowload to your computer

You need to access the [link](https://github.com/tesseract-ocr/tessdata) and select the Vietnamese language, which is the file name **vie.traineddata** downloaded and copied to the language directory of Tess OCR.

The language folder named tessdata is located in the Tesserac OCR installation directory. In general, there is a folder called tessdata on your computer anyway, please find it and copy the file **vie.traineddata** into that tessdata folder.

With Window you can dowload language when install Tesseract at Choose Components window:

![Window](Image\tesseract_install_window.jpg)

Select Vietnamese or what ever language you want at additional language data

### 2.3 Runing code

You will need to install several libary:

```pip install pytesseract```

```pip install opencv-python```

Open OCRWithTesseract.py and running code, You can change The value of the variable "filename" by path to image you want to detect and preprocess if you want to using preprocess
+ blur: Blur the image to reduce noise
+ thresh: Split black and white""" 