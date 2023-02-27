import os
import shutil
from random import sample

path = r"S:\Projects\Indian Currency classification\data"
train_path = path+"\\train"

files = os.listdir(train_path)

for note in files:
    folder_path = train_path +"\\"+note
    # print(os.listdir(folder_path))
    random_list = sample(os.listdir(folder_path),45) #30% of 150 images is 45
    # print(f"{note}--> {random_list}")
    for file in random_list:
        shutil.move(folder_path+"\\"+file,path+"\\test\\"+note+"\\"+file)
