import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create the dropdown menu
        self.options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
        self.selected_options = []
        self.dropdown = tk.Listbox(self, selectmode=tk.MULTIPLE, exportselection=0)
        for option in self.options:
            self.dropdown.insert(tk.END, option)
        self.dropdown.pack(side="left")

        # Create the button to add selected items to the list
        self.add_button = tk.Button(self, text="Add selected", command=self.add_selected)
        self.add_button.pack(side="left")

        # Create the listbox to display the selected items
        self.selected_box = tk.Listbox(self)
        self.selected_box.pack(side="left")

        # Create the button to submit the selected items
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_selected)
        self.submit_button.pack(side="left")

    def add_selected(self):
        # Add selected items to the selected options list
        selected = self.dropdown.curselection()
        for index in selected:
            option = self.options[index]
            if option not in self.selected_options:
                self.selected_options.append(option)
                self.selected_box.insert(tk.END, option)

    def submit_selected(self):
        # Submit the selected options list
        self.master.destroy()
        print(self.selected_options)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
