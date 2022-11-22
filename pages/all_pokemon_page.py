import customtkinter as ctk

from pages.pokemon import PokemonPage


class AllPokemonPage(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def switchPageTest(self):
        self.destroy()
        self.master.frame_right = PokemonPage(pokemon_id=1)  # Define the Pokemon ID we want to show
        self.master.frame_right.setup()

    def setup(self):
        self.master.text = ctk.CTkTextbox(master=self)
        self.master.text.grid(row=0, column=0)

        self.master.button_test = ctk.CTkButton(master=self, text="Pokemon ",
                                                fg_color=self.fg_color,
                                                command=self.switchPageTest,
                                                hover=False)
        self.master.button_test.place(relx=0.3, rely=0.75)
