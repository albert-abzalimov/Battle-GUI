import tkinter as tk

class Screen_Battle (tk.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        # attack button
        self.attack_button = tk.Button(self, text = "Attack", fg="Red", bg="Black", command=self.attack_clicked, height = 2, width=7)
        self.attack_button.grid(row=0, column = 0, sticky=tk.N)
        
        # Result labels
        self.result_text1 = tk.Label(self, text="", font="Times 13")
        self.result_text1.grid(row=0, column=1)
        self.result_text2 = tk.Label(self, text="", font="Times 13")
        self.result_text2.grid(row=1, column=1)
        
        # Victor label
        self.victor = tk.Label(self, text="", font="Times 13", fg = "Red")
        self.victor.grid(row=2, column=1)

        tk.Label(self, text="You").grid(row=3, column = 0, sticky=tk.S)
        tk.Label(self, text="Computer").grid(row=3, column = 1, sticky=tk.S)

        # Player 1 Image
        image_big = tk.PhotoImage(file = "images/" + self.player1.large_image)
        player1_image_label = tk.Label(self, image = image_big)
        player1_image_label.photo = image_big
        player1_image_label.grid(row=4, column=0, rowspan=3, sticky=tk.N)

        # Player 2 Image
        image_big = tk.PhotoImage(file = "images/" + self.player2.large_image)
        player1_image_label = tk.Label(self, image = image_big)
        player1_image_label.photo = image_big
        player1_image_label.grid(row=4, column=1, rowspan=3, sticky=tk.N)
        
        # HP
        self.player1_hit_points_label = tk.Label(self, text=f"{self.player1.hit_points}/{self.player1_max_hp} HP")
        self.player1_hit_points_label.grid(row=7, column = 0, sticky=tk.N)
        self.player2_hit_points_label = tk.Label(self, text=f"{self.player2.hit_points}/{self.player2_max_hp} HP")
        self.player2_hit_points_label.grid(row=7, column = 1, sticky=tk.N)
        

    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''        
        self.result_text1["text"] = self.player1.attack(self.player2)
        self.result_text2["text"] = self.player2.attack(self.player1)
        # Update
        self.player1_hit_points_label["text"] = f"{self.player1.hit_points}/{self.player1_max_hp} HP"
        self.player2_hit_points_label["text"] = f"{self.player2.hit_points}/{self.player2_max_hp} HP"
        if self.player1.hit_points <= 0:
            # Human wins, destroy attack button, and create exit button
            self.victor["text"] = "Human is victorious"
            self.attack_button.destroy()    
            self.player1_hit_points_label["text"] = f"0/{self.player1_max_hp} HP"
            tk.Button(self, text = "Exit", width=7, height = 2, command = self.exit_clicked, fg = "Red", bg = "Black").grid(row = 8, column = 1, sticky = tk.SE)

        elif self.player2.hit_points <= 0:
            # Computer wins
            self.victor["text"] = "Computer is victorious"
            self.attack_button.destroy()
            self.player2_hit_points_label["text"] = f"0/{self.player2_max_hp} HP"
            tk.Button(self, text = "Exit", width=7, height = 2, command = self.exit_clicked, fg = "Red", bg = "Black").grid(row = 8, column = 1, sticky = tk.SE)
        
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
  
            
            
            
            