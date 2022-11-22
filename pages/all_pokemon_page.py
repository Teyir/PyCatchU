import customtkinter


class AllPokemonPage(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def setup(self):
        self.text = customtkinter.CTkTextbox(master=self)
        self.text.grid(row=0, column=0)

