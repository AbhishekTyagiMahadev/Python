import os

if(not os.path.exists("Data")):
    os.mkdir("Data")
else:
    print("Folder already exist")


# os.rename("Data/Another2", f"Data/Folder1")

fold = os.listdir("Data")
print(fold)