# coding:utf-8

from PIL import Image,ImageGrab
import pytesseract,pymouse
from card_effect_search import search_card

def translate_card():
    current_card_name = ''
    while True:
        ss_region = (651*1.25, 253*1.25, 928*1.25, 278*1.25) #距离左上右下的像素
        ss_img = ImageGrab.grab(ss_region)
        pic_name = "./img/PILImage.jpg"
        ss_img.save(pic_name)

        text = pytesseract.image_to_string(Image.open(pic_name))
        if current_card_name == text:
            continue
        current_card_name = text
        print('\n-------------------------\n', current_card_name)
        try:
            search_card(current_card_name)
        except Exception as e:
            pass

if __name__ == '__main__':

    # m = pymouse.PyMouse()
    # while True:
    #     print(m.position(), end='\r')

    # ss_region = (651*1.25, 253*1.25, 928*1.25, 278*1.25) #距离左上右下的像素
    # ss_img = ImageGrab.grab(ss_region)
    # pic_name = "./img/PILImage.jpg"
    # ss_img.save(pic_name)

    # text = pytesseract.image_to_string(Image.open(pic_name))
    # print(text)
    # search_card(text)
    translate_card()