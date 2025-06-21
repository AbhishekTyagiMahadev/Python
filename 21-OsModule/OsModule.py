import os

if(not os.path.exists("Data1")):
    os.mkdir("Data1")
    os.mkdir("Data2")

for i in range(10):
    if(not os.path.exists(f"Data\Data{i+1}")):
        os.mkdir(f"Data\Data{i+1}")
    