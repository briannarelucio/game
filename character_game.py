import Tkinter as tk


class Application(tk.Frame, object):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()

        self.canvas = tk.Canvas(self, width=1000, height=700, bg="white")
        self.canvas.grid()

        self.imagePredix = tk.PhotoImage(file="predix.gif")
        self.imageVirus = tk.PhotoImage(file="virus.gif")

        #hero
        self.player = self.canvas.create_image(50, 350, image=self.imagePredix)

        #enemies
        enemy1 = self.canvas.create_image(500, 350, image=self.imageVirus)
        enemy2 = self.canvas.create_image(300, 150, image=self.imageVirus)
        enemy3 = self.canvas.create_image(750, 500, image=self.imageVirus)

        #add enemy to a list to prep collision checking
        self.enemyList = []
        self.enemyList.append(enemy1)
        self.enemyList.append(enemy2)
        self.enemyList.append(enemy3)

        #bind keyboard to key function and focus input on canvas
        self.canvas.bind("<Key>", self.key)
        self.canvas.focus_set()
        
        self.gameLoop()

    def key(self, event):
        if event.keysym == "Up" or event.keysym == "w":
            self.canvas.move(self.player, 0, -20)
        elif event.keysym == "Down" or event.keysym == "s":
            self.canvas.move(self.player, 0, 20)
        elif event.keysym == "Left" or event.keysym == "a":
            self.canvas.move(self.player, -20, 0)
        elif event.keysym == "Right" or event.keysym == "d":
            self.canvas.move(self.player, 20, 0)
        self.canvas.update()

    def gameLoop(self):
        coords = self.canvas.bbox(self.player)
        collisions = self.canvas.find_overlapping(coords[0],
                                                  coords[1],
                                                  coords[2],
                                                  coords[3])
        for collision in collisions:
            if collision in self.enemyList:
                self.canvas.delete(collision)

        if coords[0] >=1000:
            self.canvas.move(self.player,-1000,0)

        #loop 
        self.after(20,self.gameLoop)

def main():
    root = tk.Tk()
    root.title("Predix Kills Bugs - Sample App")
    root.geometry("1000x700")
    app = Application(root)

    root.mainloop()

main()


