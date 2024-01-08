# import openpyxl
# import pandas as pd
# import os

# A = check_book = 0
# B = person = 1
# C = sayad = 2
# D = date = 3
# E = cost = 4
# F = destanation = 5
# G = Ersal = 6
# H = mmm = 7
# I = uuu = 8
# J = hhh = 9
# K = ehda = 10
# L = status = 11
# M = verbose = 12


# current_directory = os.getcwd()
# base_dir = os.path.dirname(current_directory)
# excel_dir_name = os.path.join(base_dir, "Exels", '9.25.xlsx')
# excel_file = os.path.abspath(excel_dir_name)

# wb = openpyxl.load_workbook(excel_file)

# sheet_name = '6.21'

# sheet = wb[sheet_name]

# data = list(sheet.iter_rows(values_only=True))

# start_row = 7
# end_row = sheet.mcheck_photo_row

# # print(type(data[8][0]))

# def changing_type(sheet, columnn, type):
#        for row in range(start_row, end_row):
#               cells = data[start_row][columnn]
#             #   cells.data_type = None
#               cels = sheet.cell(row = row, column = columnn)
#               cels.data_type = type

# # changing_type(sheet, 1, str)
# # print(type(data[8][0]))

# cels = sheet.cell(row = 7, column = 0)
# cel = data[7][0]

# print(cels, cel)


# # for row in range(start_row, end_row):
# #         # print(data[row][check_book])
# #         if data[row][1] == 2012 :
# #                 sheet.cell(row=row, column=sayad).value = "sayad"
# #                 sheet.cell(row=row, column=mmm).value = "mmmn"
# #                 sheet.cell(row=row, column=person).value = "person"
# #                 # sheet.cell(row=row, column=D).value = "D"
# #                 # sheet.cell(row=row, column=E).value = "E"
# #         else:
# #             print('not found')


# # new_excel_file = os.path.join(base_dir, "Exels", '9.29.xlsx')
# # wb.save(new_excel_file)
# # wb.close()
