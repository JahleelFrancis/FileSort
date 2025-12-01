import os
import csv

current_dir = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(current_dir)


file_dict = {
'images':[".jpeg",".png",".jpg"], 
'text':[".doc",".txt",".pdf",".xlsx",".docx",".xls"],
'videos':[".mp4",".mkv",".gif"],
'sounds':[".mp3",".wav",".m4a"],
'applications':[".exe",".lnk"],
'codes':[".c",".py",".java",".cpp",".js",".html",".css",".php"]
}

img_list = []
txt_list = []
vid_list = []
snd_list = []
app_list = []
code_list = []


def file_sort(files: list, file_type: list, type_list: list) -> list:
    if not files:
        return type_list
    
    current_file = files[0]
    remaining_files = files[1:]
    
    lower_name = current_file.lower() # Normalize to lowercase for extension matching

    for x in file_type:
        if current_file.endswith(x):
            type_list.append(current_file)
            break

    return file_sort(remaining_files, file_type, type_list)

img_list = file_sort(files, file_dict['images'], img_list)
txt_list = file_sort(files, file_dict['text'], txt_list)
vid_list = file_sort(files, file_dict['videos'], vid_list)
snd_list = file_sort(files, file_dict['sounds'], snd_list)
app_list = file_sort(files, file_dict['applications'], app_list)
code_list = file_sort(files, file_dict['codes'], code_list)

type_dict = {
    "Images": img_list,
    "Text": txt_list,
    "Videos": vid_list,
    "Sounds": snd_list,
    "Applications": app_list,
    "Codes": code_list
}

print(type_dict)

with open(os.path.join(current_dir,'sortedFiles.csv'), 'w', newline='', encoding= 'utf-8') as sortedFiles:
    w = csv.writer(sortedFiles)
    w.writerow(["Category", "File Name"])  # header row
    for (category, file_list) in type_dict.items():
        for file_name in file_list:
            w.writerow([category, file_name])







