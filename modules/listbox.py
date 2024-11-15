import customtkinter as ctk
import tkinter as tk


class CtkHoverSelectListbox(tk.Listbox):
    def __init__(self, master=None, data=None, **kwargs):
        super().__init__(master, **kwargs)
        self.data = data if data is not None else []
        self.last_index = None

        # Привязываем события
        self.bind("<Motion>", self.on_motion)  # Наведение мыши

        # Заполняем Listbox элементами из начального списка данных
        self.refresh()

    def on_motion(self, event):
        """Обработчик наведения мыши на элемент"""
        index = self.nearest(event.y)
        if index != self.last_index:
            #print(f"Наведен на элемент с индексом: {index}")
            self.last_index = index

    def on_select(self, event):
        """Обработчик выбора элемента"""
        selected_indices = self.curselection()
        if selected_indices:
            print(f"Выбран элемент с индексом: {selected_indices[0]}")

    def refresh(self):
        """Обновление содержимого Listbox на основе текущего списка данных"""
        self.delete(0, tk.END)
        for item in self.data:
            self.insert(tk.END, item)

    def sync_with_data(self, new_data):
        """Оптимизированное обновление Listbox в соответствии с новым списком данных"""
        if new_data != self.data:
            self.data = new_data[:]
            self.refresh()

    def add_item(self, item):
        """Добавление нового элемента в список и обновление Listbox"""
        self.data.append(item)
        self.insert(tk.END, item)

    def remove_item(self, index):
        """Удаление элемента по индексу из списка и Listbox"""
        if 0 <= index < len(self.data):
            self.data.pop(index)
            self.delete(index)
