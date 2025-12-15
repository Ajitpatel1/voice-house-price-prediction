import numpy as np 
import win32com.client as wincl 
import time 

speak = wincl.Dispatch("SAPI.spvoice")

X = np.array([700 , 800 , 900 , 1000 , 1200 , 1400 , 1500])
y = np.array([25 , 30 , 35 , 45 , 55 , 65 , 75])

x_mean = np.mean(X)
y_mean = np.mean(y)

b1 = np.sum((X - x_mean) * (y - y_mean)) / sum((X - x_mean)**2)
b0 = y_mean - b1 * x_mean

speak.Speak("plese Enter your name ")
name = input("plese Enter your name : ")

speak.Speak("Enter your House Areas ")
area_user_input = int(input("Enter House Area : "))
if area_user_input <= -0 :
    speak.Speak("Plese give me valied house areas ")
    print("Plese give me valied house areas ")

exit

speak.Speak("plese wait 5 second iam just calculating your house price ")
print("plese wait 5 second iam just calculating your house price ")
time.sleep(5)

price_pridection = b0 + b1 * area_user_input

speak.Speak("hello"+name)
speak.Speak("your house price calculating process completed")
print(f"hello {name} your house price calculating process completed : ")

time.sleep(2)
speak.Speak("your predicted price on screen")
print("your predicted house price is : ", round(price_pridection , 2), "lakh ")