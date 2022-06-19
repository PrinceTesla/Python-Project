##                                           NEW COVID-19 DAILY TRACKER
import tkinter as tk
import requests
from tkinter import font
# CANVAS WIDTH AND HEIGHT 
HEIGHT = 500
WIDTH = 500
# BUTTON FUNCTION().....

def formatter(arg):
    try:
        COUNTRY = arg['country'] 
        LAST_UPDATE = arg['last_update']
        TOTAL_CASES = arg['cases']
        DEATHS = arg['deaths']
        RECOVERED = arg['recovered']
        final_view = ('COUNTRY :%s\n LAST UPDATE :%s\n TOTAL CASES IN THE COUNTRY :%s\n TOTAL DEATHS IN THE COUNTRY :%s\n RECOVERED PATIENTS :%s') %(COUNTRY,LAST_UPDATE,TOTAL_CASES,DEATHS,RECOVERED)
    except KeyError:
        return 'The Country you entered is currently not available.\n Try again.'  
    else:
        return final_view     


payload = {}
headers= {}
def get_info(country):
    url = "https://covid19-api.org/api/status/"
    response = requests.get(url+country,headers=headers,data=payload)
    view = response.json()
    view_box['text'] = formatter(view)


#API KEY = 801099b82134c20d42a25e5eeb0011ce   
#URL = api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
#URL2 = api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}
#https://covid19-api.org/api/status/:country
#https://covid19-api.org/api/country/:country
#4865a3e571msh96af02335c81d79p19a7d1jsn86d29aadcabc
#ROOT..    
root = tk.Tk()

canvas = tk.Canvas(root ,width=WIDTH,height=HEIGHT)
canvas.pack()

#BACKGROUND IMAGE ....
background_image = tk.PhotoImage(file='coronavirus.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)


#UPPER FRAME ....
upper_frame = tk.Frame(root,bg='black',bd=5)
upper_frame.place(relx=0.1,rely=0.1,relwidth=0.5,relheight=0.05,anchor='nw')

entry = tk.Entry(upper_frame,bg='white')
entry.place(relwidth=0.780,relheight=1)

button = tk.Button(upper_frame,text = 'GET',background = 'grey',fg = 'black',command=lambda:get_info(entry.get()))
button.place(relx=0.8,relwidth=0.20,relheight=1)


#LOWER FRAME ....
lower_frame = tk.Frame(root,bg='black',bd=5)
lower_frame.place(relx=0.1,rely=0.2,relwidth=0.50,relheight=0.50,anchor='nw')

view_box = tk.Label(lower_frame,bg='white',font=('monospace',15))
view_box.place(relwidth=1,relheight=1)


#label = tk.Label(frame,text='A LABEL',bg='red')
#label.place(relx=0,rely=0,relwidth=0.2,relheight=0.05)

root.mainloop()