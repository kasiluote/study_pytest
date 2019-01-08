#coding=utf-8
import os
import shutil


base_path = r'C:\Users\zyu\Pictures\backgroundPaper'

dir_list = os.listdir(base_path)

folders_path = [ base_path + "\\" + a for a in dir_list ]

os.environ.update({"__COMPAT_LAYER":"RUnAsInvoker"})

children_path = [ folder_path + "\\" + ch  for folder_path in folders_path for ch in os.listdir(folder_path) ]

print(children_path)

for a in children_path:
    for b in os.listdir(a):
        shutil.copy(a + "\\" + b ,r"C:\Users\zyu\Pictures\All")
