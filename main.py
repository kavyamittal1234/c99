import os
import shutil
path = 'C:/Users/Swati/Desktop/class99'
print("before Copying Files")
print(os.listdir (path))
source ="C:/Users/Swati/Desktop/class99/test.txt" 
destination ="C:/Users/Swati/Desktop/class99/test(copy).txt"

dest =shutil.copy(source,destination)
print("after copying files")
print(os.listdir(path))