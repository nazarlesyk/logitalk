from customtkinter import *
from PIL import Image

class AuthWindow(CTk)
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.title("Вхід")
        self.resianble(True, False)

        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side = "left", fill = "both")
        img_ctk = CTkImage(light_image=image.open("bg.png"), size = (450, 400)
        self.img_label = CTklabel(self.left_frame, text = "Welcome", image=img_ctk, font = ("Helvetica", 60, "bold"))
        self.img_label.pack()

        main_font = ("Helvetica", 20, "bold")
        self.right_frame = CTkFrame(self, fg_color="white")
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side="right", fill="both", expand="True")

        CTkLabel(self.right_frame, text="LogiTalk", font=main_font, text_color="6753cc").pack(pady=60)

        self.name_entry = CTkEntry(self.right_frame, placeholder_text="ім`я")
                                   height=45 , font=main_font,corner_radius=25, fg_color="eae6ff", border_color="eae6ff"
                                   text_color="6753cc", placeholder_text_color="6753cc""
        self.name_entry.pack(fill="")
window = AuthWindow()
window.minloop()






