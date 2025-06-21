import os

for i in range(10):
    if(not os.path.exists(f"Data\Day{i+1}")):
        os.rename(f"Data\Data{i+1}", f"Data\Day{i+1}")
