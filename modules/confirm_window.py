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


if __name__ == "__main__":
    class App(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("400x200")
            self.title("Пример Confirm Toplevel")

            self.confirm_button = ctk.CTkButton(self, text="Открыть подтверждение", command=self.open_confirmation)
            self.confirm_button.pack(pady=50)

        def open_confirmation(self):
            confirm_window = ConfirmationWindow(self, title="Вопрос", message="Вы уверены, что хотите продолжить?")
            self.wait_window(confirm_window)
            print("Ответ:", confirm_window.result)


    app = App()
    app.mainloop()
