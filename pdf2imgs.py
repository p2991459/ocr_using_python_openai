from pdf2image import convert_from_path
import os

def pdfToimgConvertor(filepath,filename):
    images = convert_from_path(filepath)
    parent_dir = os.getcwd()
    directory = filename
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)
    print(path)
    for i in range(len(images)):
        images[i].save(path + '/' 'page' + str(i) + '.jpg', 'JPEG')
    return f"pdf is converted to images in {path} directory"