# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/13 10:17
# File : pythonWriteTxt.py
my_list = ["apple", "banana", "cherry"]

# # Open the file in write mode
# with open("my_list.txt", "w") as file:
#   # Write each item in the list to the file on a new line
#   for item in my_list:
#     file.write(item + "\n")


def list2txt(lst, name):
  try:
    txtFile = f"{name}.txt"
    with open(txtFile, "w") as file:
      # Write each item in the list to the file on a new line
      for item in lst:
        file.write(str(item) + "\n")
  except Exception as e:
    print(str(e))
    return False
  finally:
    file.close()


list2txt(my_list,"test")