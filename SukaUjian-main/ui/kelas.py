from customtkinter import *
from tkinter import *


class KelasPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(column=0, row=0)
        
        self.navigation_frame = CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.insert_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Insert Kelas",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.insert_button_event)
        self.insert_button.grid(row=1, column=0, sticky="ew")

        self.update_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Update Kelas",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.update_button_event)
        self.update_button.grid(row=2, column=0, sticky="ew")

        self.delete_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Delete Kelas",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.delete_button_event)
        self.delete_button.grid(row=3, column=0, sticky="ew")

        self.select_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Select Kelas",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.select_button_event)
        self.select_button.grid(row=4, column=0, sticky="ew")

        # create insert frame
        self.insert_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.insert_frame.grid_columnconfigure(0, weight=1)

        self.insert_nomer_frame = CTkFrame(self.insert_frame)
        self.insert_nomer_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.insert_nomer_label = CTkLabel(master=self.insert_nomer_frame, text= "Masukkan Nomer Kelas: ")
        self.insert_nomer_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.insert_nomer_entry = CTkEntry(master=self.insert_nomer_frame, placeholder_text= 'Nomer Kelas')
        self.insert_nomer_entry.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="")
        
        self.insert_kapasiti = CTkScrollableFrame(self.insert_frame, orientation="vertical", label_text="Kapasiti Kelas: ")
        self.insert_kapasiti.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.selected_value = IntVar()
        for i in range(20, 61):
            CTkRadioButton(self.insert_kapasiti, text=f"{i}", value=i, variable=self.selected_value ).grid(row=i-20, padx=10, pady=10)

        self.insert_dipakai_frame = CTkFrame(self.insert_frame)
        self.insert_dipakai_frame.grid(row=3, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = IntVar(value=0)
        self.insert_dipakai_label = CTkLabel(master=self.insert_dipakai_frame, text="Adakah Kelas Ini Sudah Dipakai")
        self.insert_dipakai_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.insert_dipakai_button_1 = CTkRadioButton(master=self.insert_dipakai_frame, text= "True", variable=self.radio_var, value=0)
        self.insert_dipakai_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.insert_dipakai_button_2 = CTkRadioButton(master=self.insert_dipakai_frame, text= "False", variable=self.radio_var, value=1)
        self.insert_dipakai_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        # create update frame
        self.update_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.update_frame.grid_columnconfigure(0, weight=1)

        self.update_nomer_frame = CTkFrame(self.update_frame)
        self.update_nomer_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.update_nomer_label = CTkLabel(master=self.update_nomer_frame, text= "Masukkan Nomer Kelas yang mau diperbarui: ")
        self.update_nomer_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.update_nomer_entry = CTkEntry(master=self.update_nomer_frame, placeholder_text= 'Nomer Kelas')
        self.update_nomer_entry.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="w")
        
        self.update_nomer_baru_frame = CTkFrame(self.update_frame)
        self.update_nomer_baru_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.update_nomer_baru_label = CTkLabel(master=self.update_nomer_baru_frame, text= "Masukkan Nomer Kelas yang baru: ")
        self.update_nomer_baru_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.update_nomer_baru_entry = CTkEntry(master=self.update_nomer_baru_frame, placeholder_text= 'Nomer Kelas Baru')
        self.update_nomer_baru_entry.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="w")

        self.update_kapasiti = CTkScrollableFrame(self.update_frame, orientation="vertical", label_text="Kapasiti Kelas: ")
        self.update_kapasiti.grid(row=3, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.selected_value = IntVar()
        for i in range(20, 61):
            CTkRadioButton(self.update_kapasiti, text=f"{i}", value=i, variable=self.selected_value ).grid(row=i-20, padx=10, pady=10)

        self.update_dipakai_frame = CTkFrame(self.update_frame)
        self.update_dipakai_frame.grid(row=4, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = IntVar(value=0)
        self.update_dipakai_label = CTkLabel(master=self.update_dipakai_frame, text="Adakah Kelas Ini Sudah Dipakai")
        self.update_dipakai_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.update_dipakai_button_1 = CTkRadioButton(master=self.update_dipakai_frame, text= "True", variable=self.radio_var, value=0)
        self.update_dipakai_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.update_dipakai_button_2 = CTkRadioButton(master=self.update_dipakai_frame, text= "False", variable=self.radio_var, value=1)
        self.update_dipakai_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")


        # create delete frame
        self.delete_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.delete_frame.grid_columnconfigure(0, weight=1)

        self.delete_nomer_frame = CTkFrame(self.delete_frame)
        self.delete_nomer_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.delete_nomer_label = CTkLabel(master=self.delete_nomer_frame, text= "Masukkan Nomer Kelas yang mau dihapus: ")
        self.delete_nomer_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        self.delete_nomer_entry = CTkEntry(master=self.delete_nomer_frame, placeholder_text= 'Nomer Kelas')
        self.delete_nomer_entry.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="w")

        # create select frame
        self.select_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.select_frame.grid_columnconfigure(0, weight=1)

        self.select_nomer_frame = CTkFrame(self.select_frame)
        self.select_nomer_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.select_nomer_label = CTkLabel(master=self.select_nomer_frame, text= "Nomer Kelas yang terdaftar di Database: ")
        self.select_nomer_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        # self.select_nomer_entry = CTkEntry(master=self.select_nomer_frame, placeholder_text= 'Nomer Kelas')
        # self.select_nomer_entry.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="w")

        # select default frame
        self.select_frame_by_name("Insert")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.insert_button.configure(fg_color=("gray75", "gray25") if name == "Insert" else "transparent")
        self.update_button.configure(fg_color=("gray75", "gray25") if name == "Update" else "transparent")
        self.delete_button.configure(fg_color=("gray75", "gray25") if name == "Delete" else "transparent")
        self.select_button.configure(fg_color=("gray75", "gray25") if name == "Select" else "transparent")

        # show selected frame
        if name == "Insert":
            self.insert_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.insert_frame.grid_forget()
        if name == "Update":
            self.update_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.update_frame.grid_forget()
        if name == "Delete":
            self.delete_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.delete_frame.grid_forget()
        if name == "Select":
            self.select_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.select_frame.grid_forget()

    def insert_button_event(self):
        self.select_frame_by_name("Insert")

    def update_button_event(self):
        self.select_frame_by_name("Update")

    def delete_button_event(self):
        self.select_frame_by_name("Delete")

    def select_button_event(self):
        self.select_frame_by_name("Select")