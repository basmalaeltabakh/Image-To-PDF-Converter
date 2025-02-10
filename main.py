import tkinter as tk
from Converter import ImageToPdfConverter  

def main():
    root = tk.Tk()
    root.title("Image to PDF")
    root.geometry("600x550")
    converter = ImageToPdfConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
