# About FileSort
FileSort is a simple Python tool that scans a directory and automatically sorts its files into categories such as Images, Videos, Text Files, Applications, Code Files, and more. The results are printed to the terminal and saved into a sortedFiles.csv file for easy viewing.

--------------------------------------------------------------------------------------------------------------------
Features:

Automatically scans the folder where the script is located

Groups files by type using extension-based filtering

Uses a recursive sorting function (your file_sort() logic)

Supports common file categories:

Images (.png, .jpg, …)

Documents (.pdf, .txt, .docx, …)

Videos (.mp4, .mkv, …)

Audio (.mp3, .wav, …)

Applications (.exe, .lnk)

Code files (.py, .c, .cpp, …)

Skips directories (no folder scanning)

Saves results to a clean CSV file (Category, FileName)

Encodes output in UTF-8 so filenames with special characters work

--------------------------------------------------------------------------------------------------------------------
How it works:

The script finds its own directory with:

current_dir = os.path.dirname(os.path.abspath(__file__))


It lists all items in that folder and filters out directories.

For each file, the script recursively checks whether the filename ends with an extension from one of the defined categories.

The results are stored in a dictionary and printed.

A sortedFiles.csv file is created in the same directory as the script.

------------------------------------------------------------------------------------------------------------------- 
How to Run:

1) Clone the repository:

git clone https://github.com/your-username/FileSort.git


2) Navigate into the project folder:

cd FileSort


3) Run the script:

python fileSort.py


4) You’ll see:

The categorized file dictionary in your terminal

A sortedFiles.csv file in the same folder

-------------------------------------------------------------------------------------------------------------------
Output Example:
The generated sortedFiles.csv will look like:

Category,File Name
Images,photo1.jpg
Images,image.png
Text,notes.pdf
Applications,setup.exe
Codes,script.py

Each file is listed under its detected type.

--------------------------------------------------------------------------------------------------------------------
Technologies Used:

Python 3

os for directory operations

csv for exporting results

--------------------------------------------------------------------------------------------------------------------
License:

This project is open-source. You can use, modify, and share it freely.

