import tkinter as tk
from tkinter import ttk  # Pour un style de bouton amélioré
import random

class DiceRoller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dice Roller")
        self.geometry("600x700")  # Ajustez la taille pour mieux s'adapter aux images
        self.configure(bg='#F0F0F0')  # Couleur de fond de la fenêtre

        # Instructions pour l'utilisateur
        tk.Label(self, text="Appuyez sur le bouton pour lancer le dé !", bg='#F0F0F0').pack(pady=20)

        self.dice_images = [
            tk.PhotoImage(file='C:/Users/adrie/AppData/Local/Programs/Python/Python311/Scripts/images/dice1.png'),
            tk.PhotoImage(file='C:/Users/adrie/AppData/Local/Programs/Python/Python311/Scripts/images/dice2.png'),
            tk.PhotoImage(file='C:/Users/adrie/AppData/Local/Programs/Python/Python311/Scripts/images/dice3.png'),
            tk.PhotoImage(file='C:/Users/adrie/AppData/Local/Programs/Python/Python311/Scripts/images/dice4.png'),
            tk.PhotoImage(file='C:/Users/adrie/AppData/Local/Programs/Python/Python311/Scripts/images/dice5.png'),
            tk.PhotoImage(file='C:/Users/adrie/AppData/Local/Programs/Python/Python311/Scripts/images/dice6.png')
        ]

        # Label pour afficher l'image du dé
        self.dice_label = tk.Label(self, image=self.dice_images[0], bg='#F0F0F0')
        self.dice_label.pack(expand=True)

        # Bouton pour lancer le dé
        roll_button = ttk.Button(self, text="Roll", command=self.animate_dice)
        roll_button.pack(pady=20)

    def roll_dice(self):
        return random.randint(1, 6)

    def animate_dice(self, count=10):
        if count > 0:
            # Afficher une face de dé aléatoire
            self.dice_label.configure(image=self.dice_images[self.roll_dice() - 1])
            # Planifier le prochain changement
            self.after(100, self.animate_dice, count - 1)
        else:
            # Montrer le résultat final
            final_result = self.roll_dice()
            self.dice_label.configure(image=self.dice_images[final_result - 1])

if __name__ == "__main__":
    app = DiceRoller()
    app.mainloop()
