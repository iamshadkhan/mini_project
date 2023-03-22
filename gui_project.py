import tkinter as tk
from bot_module import create_ppt

class PPTCreatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("PPT Creator")

        # Create the GUI elements
        self.title_label = tk.Label(master, text="Title:")
        self.title_entry = tk.Entry(master)
        self.theme_label = tk.Label(master, text="Theme:")
        self.theme_dropdown = tk.OptionMenu(master, tk.StringVar(), "Theme 1", "Theme 2", "Theme 3")
        self.layout_label = tk.Label(master, text="Layout:")
        self.layout_dropdown = tk.OptionMenu(master, tk.StringVar(), "Layout 1", "Layout 2", "Layout 3")
        self.slides_label = tk.Label(master, text="Slides:")
        self.slide1_checkbox = tk.Checkbutton(master, text="Slide 1")
        self.slide2_checkbox = tk.Checkbutton(master, text="Slide 2")
        self.slide3_checkbox = tk.Checkbutton(master, text="Slide 3")
        self.create_button = tk.Button(master, text="Create PPT", command=self.create_ppt)

        # Position the GUI elements using grid layout
        self.title_label.grid(row=0, column=0)
        self.title_entry.grid(row=0, column=1)
        self.theme_label.grid(row=1, column=0)
        self.theme_dropdown.grid(row=1, column=1)
        self.layout_label.grid(row=2, column=0)
        self.layout_dropdown.grid(row=2, column=1)
        self.slides_label.grid(row=3, column=0)
        self.slide1_checkbox.grid(row=3, column=1)
        self.slide2_checkbox.grid(row=4, column=1)
        self.slide3_checkbox.grid(row=5, column=1)
        self.create_button.grid(row=6, column=1)

    def create_ppt(self):
        # Retrieve user inputs from GUI elements
        title = self.title_entry.get()
        theme = self.theme_dropdown.cget("text")
        layout = self.layout_dropdown.cget("text")
        slides = [self.slide1_checkbox, self.slide2_checkbox, self.slide3_checkbox]

        # Filter out unchecked slides
        selected_slides = []
        for slide in slides:
            if slide.instate(['selected']):
                selected_slides.append(slide.cget("text"))

        # Call the bot to create the PPT file
        create_ppt(title, theme, layout, selected_slides)

root = tk.Tk()
ppt_creator_gui = PPTCreatorGUI(root)
root.mainloop()
