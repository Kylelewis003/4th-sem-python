import os 
from zipfile import ZipFile

def zip_folder(folder_path , output_path):
    with ZipFile(output_path , 'w') as zip_obj:
        for foldername , subfolders , filenames in os.walk(folder_path):
            print("\n",foldername)
            print("\n",subfolders)
            print("\n",filenames,"\n")
            
            for i in filenames:
                file_path = os.path.join(foldername , i)
                print("---------------")
                print(file_path)
                print("---------------")
                zip_obj.write(file_path , os.path.relpath(file_path,folder_path))
                print("Iteration done")
                print("---------------")
                print("\n\n")

folder_path = "/home/neil/Downloads"

output_zip_file = '/home/neil/Downloads/downloads.deb'

zip_folder(folder_path , output_zip_file)