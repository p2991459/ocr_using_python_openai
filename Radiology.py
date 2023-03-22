import re
import cv2
import pytesseract
import os
from pdf2image import convert_from_path
import openai
class GetIntent:
    def pdfToimgConvertor(self,filepath, filename):
        images = convert_from_path(filepath)
        parent_dir = os.getcwd()
        directory = filename
        path = os.path.join(parent_dir, directory)
        os.makedirs(path)
        for i in range(len(images)):
            images[i].save(path + '/' 'page' + str(i) + '.jpg', 'JPEG')
        return path

    def imgTotextRapper(self,directoryPath):
        text = ''
        allfiles = os.listdir(directoryPath)
        Imgfilepaths = [directoryPath + '/' + file for file in allfiles]
        for filepath in Imgfilepaths:
            img = cv2.imread(filepath)
            pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
            # Adding custom options
            custom_config = r'--oem 3 --psm 6'
            text += pytesseract.image_to_string(img, config=custom_config)
        with open("text.txt", "w") as f:
            f.write(text)
        return text

    def textFormattor(self,raw_text):
        openai.api_key = "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"
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"reformat the given text\n\n text: {raw_text}",
            max_tokens=3000,
            temperature=0.2,
        )
        reformatted_text = completions["choices"][0]["text"]
        f = open("reformatted.txt", "w")
        f.write(reformatted_text)
        return reformatted_text


    def get_intentRadiology(self,reformatted_text):
        result = re.search(r'EXAM: (.+?)\n', reformatted_text)
        intent = "Can't found intent for the given Report"
        if result:
            intent = result.group(1)
        return intent




