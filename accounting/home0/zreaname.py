# import requests
# from pyzbar.pyzbar import decode
# import cv2
# import os, shutil
# import pytesseract


# current_directory = os.getcwd()
# base_dir = os.path.dirname(current_directory)
# # print(current_directory)

# check_photo_dir_name = r'C:\Users\G L S\Documents\git_hub\cheke_sayadi\Ax'
# bi_barcode_dir_name = r'C:\Users\G L S\Documents\git_hub\cheke_sayadi\Ax\bi_barcodee'
# duplicate_dir_name = r'C:\Users\G L S\Documents\git_hub\cheke_sayadi\Ax\duplicate'
# new_dir_name = os.path.join(check_photo_dir_name, "new")

# def scan_barcode(image):
#     # تشخیص بارکد در تصویر
#     barcodes = decode(image)

#     if barcodes:
#         barcode_content = barcodes[-1].data.decode('utf-8')
#         barcode_type = barcodes[-1].type
#         content = barcode_content
#         type = barcode_type
#         return content
#     else:
#         return "No barcode"


# def extract_16_from_decoder(dec:str):
#     dec = list(dec)
#     parametr = ''.join(map(str, dec[-16:]))
#     return parametr



# def read_check_images(directory):
#     image_files = os.listdir(directory)

#     for filename in image_files:
#         if filename.endswith('.jpg') or filename.endswith('.png'):
#             image_path = os.path.join(directory, filename)
#             image = cv2.imread(image_path)
#             barcode_content = scan_barcode(image)
#             if barcode_content is not None:
#                 if len(barcode_content) == 16:
#                     print("was_okey")
#                     path = os.path.join(directory, filename)
#                     shutil.move(path, os.path.join(new_dir_name, filename))
#                 else :
#                     sayd_16 = extract_16_from_decoder(barcode_content)
#                     new_filename = sayd_16 + '.jpg'
#                     new_path = os.path.join(directory, new_filename)

#                     # while os.path.exists(new_path):
#                     #     new_filename = os.path.splitext(new_filename)[0] + '0.jpg'
#                     #     new_path = os.path.join(directory, new_filename)

#                     try:
#                         os.rename(image_path, new_path)
#                         shutil.move(new_path, new_dir_name)
#                     except shutil.Error:
#                         if not os.path.exists(duplicate_dir_name):
#                             os.makedirs(duplicate_dir_name)
#                         new_path = os.path.join(duplicate_dir_name, new_filename)
#                         os.rename(image_path, new_path)
#                         shutil.move(new_path, bi_barcode_dir_name)
#             else:
#                 print("No barcode detected")
#                 path = os.path.join(directory, filename)
#                 shutil.move(path, os.path.join(bi_barcode_dir_name, filename))



# # آدرس IP و پورت مربوط به کانتینر Tesseract
# tesseract_host = '127.0.0.1'
# tesseract_port = '8888'

# # مسیر تصویر مورد نظر
# direct = r'C:\Users\G L S\Documents\git_hub\cheke_sayadi'
# check_photo = '25.jpg'
# path = os.path.join(direct, check_photo)
# patt = r'c:\Users\G L S\Documents\git_hub\cheke_sayadi\25.jpg'
# image_path = patt

# # ارسال درخواست به کانتینر Tesseract برای استخراج متن
# response = requests.get(f'http://{tesseract_host}:{tesseract_port}/extract', params={'image_path': image_path})
# # بررسی و پردازش پاسخ
# if response.status_code == 200:
#     extracted_text = response.text
#     print(extracted_text)
# else:
#     print('Error occurred:', response.status_code)




# def extract_text_from_img(directory, filename):

#     image_path = os.path.join(directory, filename)
#     image = cv2.imread(image_path)

#     # Convert the image to grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Use pytesseract to extract text from the grayscale image
#     text = pytesseract.image_to_string(gray_image)

#     # Print the extracted text
#     print(text)




# def extract_text_from_image(image_path):
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     text = pytesseract.image_to_string(gray)
#     return text

# # مثال استخراج متن از یک تصویر
# image_path = 'path_to_your_image.jpg'
# text = extract_text_from_image(image_path)
# print(text)



# def extract_id(barcode_content):
#         # جستجوی آخرین زیررشته عددی

#     print('adasdadadadads',barcode_content)
#     last_numeric_substring = ''
#     for substring in barcode_content.split():
#         if substring.isdigit():
#             last_numeric_substring = substring

#     # بررسی طول زیررشته
#     if len(last_numeric_substring) == 16:
#         return last_numeric_substring

#     return None


# id_16_digits = extract_id(a)

# if id_16_digits:
#     print("16-digit ID:", id_16_digits)
# else:
#     print("No 16-digit ID found")



# # def extract_id(barcode_content):
# #     # جستجوی آخرین زیررشته عددی با طول 16
# #     id_16_digits = ''
# #     for character in reversed(barcode_content):
# #         if character.isdigit():
# #             id_16_digits = character + id_16_digits
# #             if len(id_16_digits) == 16:
# #                 return id_16_digits

# #     return None

# # # مثال استفاده از تابع
# # # barcode_content = "01 1 2181234272 IR740140040000013000412521 1401266-14 165653 2590020025133201"
# # id_16_digits = extract_id(a)

# # if id_16_digits:
# #     print("16-digit ID:", id_16_digits)
# # else:
# #     print("No 16-digit ID found")










# # read_check_images(current_directory + 'Ax_ha')



# # def read_check_id(image):
# #     # انجام پردازش و استخراج شناسه 16 رقمی از عکس
# #     # کد خواندن شناسه 16 رقمی را اضافه کنید

# #     return check_id

# # # مسیر پوشه عکس های چک
# # check_images_directory = '/path/to/check/images'

# # # فراخوانی تابع برای خواندن عکس ها و تغییر نام فایل ها
# # read_check_images(check_images_directory)s
