import sys
from PIL import Image, ImageFilter, ImageEnhance
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader

def main():
    if len(sys.argv) < 2:
        sys.exit('You must specify a file path for the pdf file.')

    file_input = sys.argv[1]
    pages = convert_from_path(file_input, 350)

    i = 1
    for page in pages:
        image_name = "Page_" + str(i) + ".jpg"
        page.save(image_name, "JPEG")
        i = i+1

    image_path = 'Page_1.jpg'

    image = Image.open(image_path)

    image = image.convert('L')

    image = image.filter(ImageFilter.SHARPEN)

    brightness_enhancer = ImageEnhance.Brightness(image)
    image = brightness_enhancer.enhance(1.5)

    color_enhancer = ImageEnhance.Color(image)
    image = color_enhancer.enhance(5)

    contrast_enhancer = ImageEnhance.Contrast(image)
    image = contrast_enhancer.enhance(5)

    text = pytesseract.image_to_string(image)

    # Prints the text
    print(text)


if __name__ == "__main__":
    main()

