import tkinter
from turtle import width

class Screen_CharacterSelection (tkinter.Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
       # Save the CharacterRoster  
        self.roster = roster
        # Save the method reference to which we return control after the player hits "Character Selected"
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        The information about each character should be derived from self.roster, 
        which is a CharacterRoster loaded from battle_characters.txt. 
        The layout should NOT be hard-coded: if you re-order, alter, or remove entries 
        in battle_characters.txt, the layout should automatically reflect those changes. 
        
        ########
        
        The radio buttons on this page should all use the variable "self.character_index_index".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character_index would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character_index has been instantiated for your convenience below.
        
        ########

        Here is some sample code for including an image on a page:   (char is a Character object)
            
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.

            w.grid (ADD PARAMETERS HERE)
        '''
        # Top of the graph
        tkinter.Label(self, text="Hit Points", font = "Times 13").grid(row=0, column=3, sticky=tkinter.N)
        tkinter.Label(self, text="Dexterity", font = "Times 13").grid(row=0, column=4, sticky=tkinter.N)
        tkinter.Label(self, text="Strength", font = "Times 13").grid(row=0, column=5, sticky=tkinter.N)


        self.character_index = tkinter.StringVar()
        self.character_index.set(None)
        
        for i in range(len(self.roster.character_list)):
            tkinter.Radiobutton(self, text = self.roster.character_list[i].name, value = i, variable=self.character_index).grid(row=i + 1, column=0, sticky = tkinter.W)
            image_small = tkinter.PhotoImage(file = "images/" + self.roster.character_list[i].small_image)
            new_image = tkinter.Label(self, image = image_small)
            new_image.photo = image_small
            new_image.grid(row=i + 1, column=1, sticky = tkinter.W)
            tkinter.Label(self, text = str(self.roster.character_list[i].hit_points), font = "Arial 16").grid(row = i+1, column=3, sticky = tkinter.NS)
            tkinter.Label(self, text = str(self.roster.character_list[i].strength), font = "Arial 16").grid(row = i+1, column=4, sticky = tkinter.NS)
            tkinter.Label(self, text = str(self.roster.character_list[i].dexterity), font = "Arial 16").grid(row = i+1, column=5, sticky = tkinter.NS)
        self.commence_battle_button = tkinter.Button(self, text="Select a Character!", bg="Orange", fg="Purple", width=20, height = 2, command=self.selected_clicked)
        self.commence_battle_button.grid(column=3, columnspan=4)
    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''    
        try:
            self.callback_on_selected(self.character_index.get()) 
        except:
            self.commence_battle_button["text"] = "Select a Character First"
            
        