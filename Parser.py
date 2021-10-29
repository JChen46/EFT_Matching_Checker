import pyautogui
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/John Chen/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

def Parser(region, keywords):
    region_img = pyautogui.screenshot(region=region)
    # region_img.save('what.png')
    raw_text = pytesseract.image_to_string(region_img)
    processed_text = re.sub('[^a-zA-Z ]', "", raw_text)
    print(processed_text, flush=True)
    
    try:
        # if(element for element in keywords if(element in processed_text.lower())):
        for key in keywords:
            if(key in processed_text.lower()):
                print('\nFOUND: %s' % key, flush=True)
                return True
        else:
            return False
    except ValueError:
        print('ERROR: ValueError', flush=True)
        pass
