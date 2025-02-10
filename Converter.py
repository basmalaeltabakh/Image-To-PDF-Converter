import tkinter as tk
from tkinter import filedialog, messagebox
import os
from reportlab.pdfgen import canvas
from PIL import Image


class ImageToPdfConverter:
    def __init__(self, root):
        self.root = root
        self.imagePaths = []
        self.outputPDFName = tk.StringVar()
        self.selectedImageListBox = tk.Listbox(root, selectmode=tk.MULTIPLE, bg="black", fg="yellow")
        self.initialize_ui()


    def initialize_ui(self):
        self.root.configure(bg="black")  

        titleLabel = tk.Label(self.root, text="Image to PDF Converter", font=("Helvetica", 20, "bold"), bg="black", fg="White")
        titleLabel.pack(pady=10)

        selectImagesButton = tk.Button(self.root, text="Select Images", command=self.selectedImages, bg="White", fg="black")
        selectImagesButton.pack(pady=(0, 10))

        self.selectedImageListBox.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

        label = tk.Label(self.root, text="Enter Output PDF name:", bg="black", fg="White")
        label.pack()
        PDFnameEntry = tk.Entry(self.root, textvariable=self.outputPDFName, width=40, justify='center', bg="black", fg="White", insertbackground="White")
        PDFnameEntry.pack()

        convertButton = tk.Button(self.root, text="Convert to PDF", command=self.ConvertImagesToPdf, bg="White", fg="black")
        convertButton.pack(pady=(20, 40))


    def selectedImages(self):
        self.imagePaths = filedialog.askopenfilenames(title="Select Images",
                                                      filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.updateSelectedImagesListBox()


    def updateSelectedImagesListBox(self):
        self.selectedImageListBox.delete(0, tk.END)
        for imagePath in self.imagePaths:
            _, imageName = os.path.split(imagePath)
            self.selectedImageListBox.insert(tk.END, imageName)


    def ConvertImagesToPdf(self):
        if not self.imagePaths:
            messagebox.showerror("Error", "No images selected!")
            return


        outputPdfPath = self.outputPDFName.get() + ".pdf" if self.outputPDFName.get() else "output.pdf"
        self.create_pdf(self.imagePaths, outputPdfPath)

        messagebox.showinfo("Success", f"PDF saved as {outputPdfPath}")


    def create_pdf(self, images, pdf_name):
        if not images:
            return  

        pdf = canvas.Canvas(pdf_name, pagesize=(612, 792))


        for imagePath in images:
            img = Image.open(imagePath).convert("RGB")
            availableWidth = 540
            availableHeight = 720
            scale_factor = min(availableWidth / img.width, availableHeight / img.height)
            newWidth = img.width * scale_factor
            newHeight = img.height * scale_factor
            Xcentered = (612 - newWidth) / 2
            Ycentered = (792 - newHeight) / 2

            pdf.drawImage(imagePath, Xcentered, Ycentered, width=newWidth, height=newHeight)
            pdf.showPage()

        pdf.save()
