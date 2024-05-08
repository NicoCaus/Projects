import os
from pathlib import Path

# folder path, should config for yourself
dwnlds_path = "C:/Users/nicoc/Downloads"
dir_compr = "C:/Users/nicoc/Downloads/Comprimidos"
dir_aud_vid = "C:/Users/nicoc/Downloads/Audios y Videos"
dir_img = "C:/Users/nicoc/Downloads/Imagenes"
dir_docs = "C:/Users/nicoc/Downloads/Documentos"
dir_exes = "C:/Users/nicoc/Downloads/Ejecutables"
dir_other = "C:/Users/nicoc/Downloads/Otros"
dir_list = [dwnlds_path,dir_compr, dir_aud_vid, dir_img, dir_docs, dir_exes, dir_other]

#extension lists
ext_compr = ['zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz']
ext_aud_vid = ['mp4', 'avi', 'mov', 'mkv', 'wmv', 'flv', 'mpg', 'webm', 'ogg', '3gp','mp3', 'wav', 'ogg', 'flac', 'aac', 'm4a', 'wma', 'aiff', 'opus', 'ape']
ext_img = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg', 'ico']
ext_docs = ['pdf', 'doc', 'docx', 'txt', 'rtf', 'xls', 'xlsx', 'ppt', 'pptx', 'odt']
ext_exes = ['exe', 'msi', 'bat']

#Checks if inputed paths exist
def folder_checker():
    global dir_list
    check = 0
    for dir_path in dir_list:
        if not Path(dir_path).exists():
            check = 1
    if check == 1:
        return False
    else:
        return True

if folder_checker():
    # list to store files
    res = []
    # Iterate directory
    for file in os.listdir(dwnlds_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dwnlds_path, file)):
            res.append(file)
            if any(file.endswith(ext) for ext in ext_compr):
                os.replace(f"{dwnlds_path}/{file}", f"{dir_compr}/{file}")
            elif any(file.endswith(ext) for ext in ext_aud_vid):
                os.replace(f"{dwnlds_path}/{file}", f"{dir_aud_vid}/{file}")
            elif any(file.endswith(ext) for ext in ext_img):
                os.replace(f"{dwnlds_path}/{file}", f"{dir_img}/{file}")
            elif any(file.endswith(ext) for ext in ext_docs):
                os.replace(f"{dwnlds_path}/{file}", f"{dir_docs}/{file}")
            elif any(file.endswith(ext) for ext in ext_exes):
                os.replace(f"{dwnlds_path}/{file}", f"{dir_exes}/{file}")
            elif file.endswith(".temp") or file.endswith(".crdownload") or file[0:2] == "~$":
                pass
            else:
                os.replace(f"{dwnlds_path}/{file}", f"{dir_other}/{file}")

else:
    print("Selected Folders dont exist")
