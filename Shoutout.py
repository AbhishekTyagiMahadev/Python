# from os import system
# system("say hello")
import win32com.client

list = ['Abhishek', 'Vivek', 'Tanu', 'Himanshi']
s = win32com.client.Dispatch("SAPI.Spvoice")
for name in list:
    s.Speak(f"Hello {name}")