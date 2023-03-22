import cv2
import pytesseract
import os
img = cv2.imread('page0.jpg')
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
# Adding custom options
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)
with open("text.txt", "w") as f:
    f.read(f.write(text))
print(text)

def textRapper(directoryPath):
    text = ''
    allfiles = os.listdir(directoryPath)
    Imgfilepaths = [directoryPath + '/' + file for file in allfiles]
    print(Imgfilepaths)
    for filepath in Imgfilepaths:
        img = cv2.imread(filepath)
        pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
        # Adding custom options
        custom_config = r'--oem 3 --psm 6'
        text += pytesseract.image_to_string(img, config=custom_config)
    with open("text.txt", "w") as f:
        f.write(text)
    print(text)
    return "text extracted and saved in text.txt"