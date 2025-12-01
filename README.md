# About FileSort
FileSort is a simple Python tool that scans a directory and automatically sorts its files into categories such as Images, Videos, Text Files, Applications, Code Files, and more. The results are printed to the terminal and saved into a sortedFiles.csv file for easy viewing.

--------------------------------------------------------------------------------------------------------------------
Features:

Automatically scans the current working directory

Categorizes files based on their extensions

Handles unknown file types with an “Other” category

Outputs results to the console

Exports sorted file data to a CSV file (sortedFiles.csv)

--------------------------------------------------------------------------------------------------------------------
Categories Included:

Images (.jpeg, .png, .jpg)

Text (.txt, .pdf, .docx, etc.)

Videos (.mp4, .mkv, .gif)

Sounds (.mp3, .wav)

Applications (.exe, .lnk)

Code Files (.py, .cpp, .js, etc.)

Other (for unmatched extensions)

------------------------------------------------------------------------------------------------------------------- How to Run:

Make sure you have Python 3 installed.

Clone the repository:

git clone https://github.com/your-username/FileSort.git


Run the script in a directory containing files:

python fileSort.py


A file called sortedFiles.csv will be generated with categorized results.

--------------------------------------------------------------------------------------------------------------------
Technologies Used:

Python 3

os for directory operations

csv for exporting results

---------------------------------------------------------------------------------------------------------------------
License:

This project is open-source. You can use, modify, and share it freely.

