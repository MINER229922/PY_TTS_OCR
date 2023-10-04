import asyncio
import winocr
from PIL import Image


async def TestFunc(pathImg, lang):
    img = Image.open(pathImg)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    # print(img.mode)
    result = await winocr.recognize_pil(img, lang)
    txt = result.text
    print(txt)


asyncio.run(TestFunc("./ocr_sample/jp-1023_1046.jpg","ja"))
asyncio.run(TestFunc("./ocr_sample/en-1477_933.jpg", 'en'))
