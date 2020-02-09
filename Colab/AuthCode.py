from captcha.image import ImageCaptcha
from PIL import Image

text = '12husdah34'
image = ImageCaptcha()
captcha = image.generate(text)
captcha_image = Image.open(captcha)
captcha_image.show()