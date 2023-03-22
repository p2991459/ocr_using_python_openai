from Radiology import GetIntent

app = GetIntent()
filepath = 'C:\\Users\\Linuxbean\\Music\\ai\\Radiology Redacted\\1_Redacted.pdf'
filename = '1_Redacted'
directorypath = app.pdfToimgConvertor(filepath,filename)
text = app.imgTotextRapper(directoryPath= directorypath)
reformatted_text = app.textFormattor(text)
intent = app.get_intentRadiology(reformatted_text)
print(intent)
