import shutil
import os
shutil.copy("ShutilModule.py", "Abhishek.py")
os.mkdir("Data")
shutil.copytree("Data", "NewData")
# shutil.move( "New","data/Another")
# shutil.rmtree("Data")
# os.remove("Abhishek.py")
print(os.listdir())