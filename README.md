# Image to PDF Converter 📑

##  Description
This project is a simple **Image to PDF Converter** built using **Python** and **Tkinter** for the GUI. It allows users to select multiple images and convert them into a single **PDF file**.




##  Project Structure
```
 ImageToPDF
├──  converter.py   # Contains all the core functions for image-to-PDF conversion
├──  main.py        # The main file to run the Tkinter application

```

##  Features
- Select multiple images (JPG, PNG, JPEG)
- Convert them into a **single PDF**
- Choose the output file name
- Simple and **dark mode** UI (black background, yellow text)
- Error handling and success messages

##  How It Works
1. Click **"Select Images"** to choose image files.
2. Enter a name for the output **PDF file** (or leave it blank to use the default name `output.pdf`).
3. Click **"Convert to PDF"** to generate the PDF.
4. A message will confirm the successful conversion, and the PDF will be saved in the same directory.

##  Tech Stack
- **Python** (Main Language)
- **Tkinter** (GUI)
- **Pillow (PIL)** (Image Processing)
- **ReportLab** (PDF Generation)







