from customtkinter import CTkToplevel
import customtkinter as ctk


class ToplevelWindow(CTkToplevel):
    def __init__(self, task: str="", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ctk.CTkLabel(self, text="Вы уверены")
        self.label.pack(padx=20, pady=20)


if __name__ == "__main__":
    class App(ctk.CTk):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("500x400")

            self.button_1 = ctk.CTkButton(self, text="open toplevel", command=self.open_toplevel)
            self.button_1.pack(side="top", padx=20, pady=20)

            self.toplevel_window = None

        def open_toplevel(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it


    app = App()
    app.mainloop()
