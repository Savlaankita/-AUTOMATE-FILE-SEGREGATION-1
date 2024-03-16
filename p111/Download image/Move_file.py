import os 
import shutil

from_dir = "C:/Users/Ankita/Downloads"
to_dir = "C:/Users/Ankita/desktop/downloadedimages"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

#Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.txt', '.pdf', '.doc', '.docx',]:

        path1 = from_dir +'/'+ file_name
        path2 = to_dir +'/' +"Image_Files"
        path3 = to_dir +'/' + "Image_Files"+'/'+file_name

        if os.path.exists(path2):
            print("Moving" + file_name +".....")

            #Move to path1 ---> path3
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
        print("Moving" + file_name +".....")
        shutil.move(path1,path3)