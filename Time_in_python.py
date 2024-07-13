from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.title("Time in py")
root.geometry("700x900")

india_image = ImageTk.PhotoImage(Image.open("india-map-2019.jpg"))
usa_image = ImageTk.PhotoImage(Image.open("USA-map.jpg"))
australia_image = ImageTk.PhotoImage(Image.open("australia-map-1400px.jpg"))
japan_image = ImageTk.PhotoImage(Image.open("japan-map.jpg"))


class India():
    def times(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        formatedTime = local_time.strftime("%H:%M:%S")
        india_time['text'] = "Time : " + formatedTime
        india_time.after(200, self.times)
        
class Usa():
    def times(self):
        home = pytz.timezone("US/Central")
        local_time = datetime.now(home)
        formatedTime = local_time.strftime("%H:%M:%S")
        usa_time['text'] = "Time : " + formatedTime
        usa_time.after(200, self.times)
        
class Australia():
    def times(self):
        home = pytz.timezone("Australia/ACT")
        local_time = datetime.now(home)
        formatedTime = local_time.strftime("%H:%M:%S")
        australia_time['text'] = "Time : " + formatedTime
        australia_time.after(200, self.times)

class Japan():
    def times(self):
        home = pytz.timezone("Asia/Tokyo")
        local_time = datetime.now(home)
        formatedTime = local_time.strftime("%H:%M:%S")
        japan_time['text'] = "Time : " + formatedTime
        japan_time.after(200, self.times)




# INDIA UI #

India_Label = Label(root, text="India")
India_Label.place(relx=0.25, rely=0.05, anchor=CENTER)

india_img = Label(root)
india_img["image"] = india_image
india_img.place(relx=0.25, rely=0.2, anchor=CENTER)

india_time = Label(root)
india_time.place(relx=0.25, rely=0.33, anchor=CENTER)

instance_of_india= India()
india_btn = Button(root, text="Show Time", command=instance_of_india.times)
india_btn.place(relx=0.2, rely=0.36)

# USA UI #

Usa_label = Label(root, text="USA")
Usa_label.place(relx=0.7, rely=0.05, anchor=CENTER)

usa_img = Label(root)
usa_img["image"] = usa_image
usa_img.place(relx=0.75, rely=0.2, anchor=CENTER)

usa_time = Label(root)
usa_time.place(relx=0.75, rely=0.33, anchor=CENTER)

instance_of_usa = Usa()
usa_btn = Button(root, text="Show Time", command=instance_of_usa.times)
usa_btn.place(relx=0.7, rely=0.36)


# INDIA UI #

australia_Label = Label(root, text="AUSTRALIA")
australia_Label.place(relx=0.25, rely=0.5, anchor=CENTER)

australia_img = Label(root)
australia_img["image"] = australia_image
australia_img.place(relx=0.25, rely=0.65, anchor=CENTER)

australia_time = Label(root)
australia_time.place(relx=0.25, rely=0.78, anchor=CENTER)

instance_of_australia= Australia()
australia_btn = Button(root, text="Show Time", command=instance_of_australia.times)
australia_btn.place(relx=0.2, rely=0.82)

# JAPAN UI #

japan_label = Label(root, text="JAPAN")
japan_label.place(relx=0.7, rely=0.5, anchor=CENTER)

japan_img = Label(root)
japan_img["image"] = japan_image
japan_img.place(relx=0.7, rely=0.65, anchor=CENTER)

japan_time = Label(root)
japan_time.place(relx=0.7, rely=0.78, anchor=CENTER)

instance_of_japan = Japan()
japan_btn = Button(root, text="Show Time", command=instance_of_japan.times)
japan_btn.place(relx=0.65, rely=0.82)

root.mainloop()