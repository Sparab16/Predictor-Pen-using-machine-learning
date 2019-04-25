import tkinter as tk
import socket
from PIL import  Image, ImageDraw

# s = socket.socket()
# host = socket.gethostname()
# port = 12345
# s.connect((host,port))
# print("Connection Established")


class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Free Hand Mode")
        self.counter = 1
        self.previous_x = self.previous_y = 0
        self.x = self.y = 0
        self.points_recorded = []
        self.canvas = tk.Canvas(self, width=400, height=400, bg = "black", cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.image1 = Image.new('RGB',(1536,580),'black')
        self.draw = ImageDraw.Draw(self.image1)
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)
        self.button_clear.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<Motion>", self.tell_me_where_you_are)
        self.canvas.bind("<B1-Motion>", self.draw_from_where_you_are)
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar)
        self.filemenu.add_command(label='Save Image', command= self.save)
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.config(menu=self.menubar)


    def save(self):
        filename = 'FreeHandMode_' + str(self.counter) + '.png'
        self.counter += 1
        self.image1.save(filename)


    def clear_all(self):
        self.canvas.delete("all")
        self.image1 = Image.new('RGB',(1536,580),'black')
        self.draw = ImageDraw.Draw(self.image1)

    def tell_me_where_you_are(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

    def draw_from_where_you_are(self, event):
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()
        self.x = event.x
        self.y = event.y
        self.canvas.create_line(self.previous_x, self.previous_y,
                                self.x, self.y,fill="yellow",width=2)
        self.draw.line([self.previous_x,self.previous_y,self.x,self.y],fill="yellow",width=2)
        self.points_recorded.append(self.previous_x)
        self.points_recorded.append(self.previous_y)
        self.points_recorded.append(self.x)
        self.points_recorded.append(self.x)
        self.previous_x = self.x
        self.previous_y = self.y


app = ExampleApp()
app.mainloop()