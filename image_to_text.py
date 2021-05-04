import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import sys
import os
d1 = False
def img_tool(droppedFile):
    image = cv2.imread(droppedFile)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image = cv2.medianBlur(image,5)
    image = cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(image)
    text = text[:-1]
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''Output:
''',text)
    input(">")
    os.system('cls' if os.name == 'nt' else 'clear')
while(1):
    if d1 == False:
        try:
            img_tool(sys.argv[1])
            d1 = True
        except IndexError:
            try:
                img_tool(input("drop file here: "))
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('''         Error
Not A Valid File Dropped''')
    else:
        try:
            img_tool(input("drop file here: "))
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''         Error
Not A Valid File Dropped''')
