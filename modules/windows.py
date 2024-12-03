from customtkinter import CTkToplevel
import customtkinter as ctk

# Класс для окна подтверждения
class ConfirmationWindow(ctk.CTkToplevel):
    def __init__(self, master, title="Подтверждение", message="Вы уверены?", buttons=("Да", "Нет")):
        super().__init__(master)
        self.title(title)
        self.resizable(False, False)

        self.result = None

        self.label = ctk.CTkLabel(self, text=message, font=("Arial", 14))
        self.label.pack(pady=20)

        # Buttons container
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        self.yes_button = ctk.CTkButton(self.button_frame, text=buttons[0], command=self.on_yes)
        self.yes_button.grid(row=0, column=0, padx=10)
        self.no_button = ctk.CTkButton(self.button_frame, text=buttons[1], command=self.on_no)
        self.no_button.grid(row=0, column=1, padx=10)

        self.after(10, self.grab_set)

    def on_yes(self):
        self.result = True
        self.destroy()

    def on_no(self):
        self.result = False
        self.destroy()


class Send_window(ctk.CTkToplevel):
    def __init__(self, master: ctk.CTk):
        super().__init__(master)
        self.title("Upload path")
        self.resizable(False, False)
        
        self.result = None
        
        self.main_grid = ctk.CTkFrame(self)
        self.main_grid.pack(padx=20)
        
        self.label = ctk.CTkLabel(self.main_grid, text="Upload path")
        self.label.grid(row=0, column=0)
        
        self.input_grid = ctk.CTkFrame(self.main_grid)
        self.input_grid.grid(row=1, column=0)
        
        self.ip_input_name = ctk.CTkLabel(self.input_grid, text="Enter ip:port")
        self.ip_input_name.grid(row=0, column=0, padx=(10, 5), pady=5)
        self.ip_input = ctk.CTkEntry(self.input_grid)
        self.ip_input.grid(row=0, column=1, padx=(5, 5), pady=5)
        self.ip_input_error = ctk.CTkLabel(self.input_grid, text="", text_color="#ff0000")
        self.ip_input_error.grid(row=0, column=2, padx=(5, 10), pady=5)
        
        self.filename_input_name = ctk.CTkLabel(self.input_grid, text="Enter path name")
        self.filename_input_name.grid(row=1, column=0, padx=(10, 5), pady=5)
        self.filename_input = ctk.CTkEntry(self.input_grid)
        self.filename_input.grid(row=1, column=1, padx=(5, 5), pady=5)
        self.filename_input_error = ctk.CTkLabel(self.input_grid, text="", text_color="#ff0000")
        self.filename_input_error.grid(row=1, column=2, padx=(5, 10), pady=5)
        
        self.confirm_button = ctk.CTkButton(self.main_grid, text="Загрузить", command=self.confirm_pressed)
        self.confirm_button.grid(row=2, column=0, padx=10, pady=5)
        
        self.after(10, self.grab_set)

    def confirm_pressed(self):
        if self.ip_input.get() == "":
            self.ip_input_error.configure(text="Введите ip")
            return
        else:
            self.ip_input_error.configure(text="")
        if self.filename_input.get() == "":
            self.filename_input_error.configure(text="Введите имя файла")
            return
        else:
            self.filename_input_error.configure(text="")
        self.result = {"ip": self.ip_input.get(), "filename": self.filename_input.get()}
        self.destroy()
        
if __name__ == "__main__":
    class App(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("400x200")
            self.title("Пример Confirm Toplevel")
            self.resizable(False, False)

            self.confirm_button = ctk.CTkButton(self, text="Открыть подтверждение", command=self.open_confirmation)
            self.confirm_button.pack(pady=50)

        def open_confirmation(self):
            confirm_window = Send_window(self)
            self.wait_window(confirm_window)
            print("Ответ:", confirm_window.result)


    app = App()
    app.mainloop()