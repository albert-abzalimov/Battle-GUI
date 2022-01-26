import tkinter as tk

class Screen_PrepareToBattle (tk.Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()


    def create_widgets (self):
        ''' This method creates all of the widgets the prepare to battle page. '''
        tk.Label(self, text="You").grid(row=0, column = 0, sticky=tk.N)
        tk.Label(self, text="Computer").grid(row=0, column = 1, sticky=tk.N)

        # Player 1 Image
        image_big = tk.PhotoImage(file = "images/" + self.player1.large_image)
        player1_image_label = tk.Label(self, image = image_big)
        player1_image_label.photo = image_big
        player1_image_label.grid(row=1, column=0, rowspan=3, )


        # Player 2 Image
        image_big = tk.PhotoImage(file = "images/" + self.player2.large_image)
        player1_image_label = tk.Label(self, image = image_big)
        player1_image_label.photo = image_big
        player1_image_label.grid(row=1, column=1, rowspan=3)
        
        tk.Label(self, text=f"{self.player1.hit_points} HP").grid(row=5, column = 0, sticky=tk.N)
        tk.Label(self, text=f"{self.player2.hit_points} HP").grid(row=5, column = 1, sticky=tk.N)

        tk.Label(self, text=f"{self.player1.dexterity} Dexterity").grid(row=6, column = 0, sticky=tk.N)
        tk.Label(self, text=f"{self.player2.dexterity} Dexterity").grid(row=6, column = 1, sticky=tk.N)

        tk.Label(self, text=f"{self.player1.strength} Strength").grid(row=7, column = 0, sticky=tk.N)
        tk.Label(self, text=f"{self.player2.strength} Strength").grid(row=7, column = 1, sticky=tk.N)
        
        tk.Button(self, text = "Commence Battle", fg="Red", bg="Black", command=self.commence_battle_clicked).grid(row=8, column = 1, sticky=tk.SE)
        '''    
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.

            w.grid (ADD PARAMETERS HERE)'''
 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        