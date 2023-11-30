import os
import shutil

user_home = os.path.expanduser("~")

src_dir = os.path.join(user_home, 'Downloads')
dest_dir_image = os.path.join(user_home, 'Pictures')
dest_dir_doc = os.path.join(user_home, 'Documents')
dest_dir_video = os.path.join(user_home, 'Videos')
dest_dir_audio = os.path.join(user_home, 'Music')

files_list = []

def move(file, dest):
    source = os.path.join(src_dir, file)
    destination = os.path.join(dest, file)
    shutil.move(source, destination)  # move
    print('Moved:', file)

basepath = src_dir
for entry in os.listdir(basepath):
    # checking if it's a file
    if os.path.isfile(os.path.join(basepath, entry)):
        files_list.append(entry)  # filename

# add more as needed
document_extensions = ('.pdf', '.asc', '.txt', '.json', '.docx', '.doc', '.pptx', '.ppt', '.xlsx', '.xls', '.xlsm', '.csv', '.eml', '.msg', '.epub', '.torrent', '.py', '.zip',)
video_extensions = ('.mp4', '.webm', '.3gpp', '.avi', '.mkv', )
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg',)
audio_extensions = ('.mp3','.flac', '.m4a', '.wav',)


for file in files_list:
    file_lower, file_ext = os.path.splitext(file.lower())

    if file_ext in document_extensions:
        move(file, dest_dir_doc)
    elif file_ext in video_extensions:
        move(file, dest_dir_video)
    elif file_ext in image_extensions:
        move(file, dest_dir_image)
    elif file_ext in audio_extensions:
        move(file, dest_dir_audio)

print('Move complete')