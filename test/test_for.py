import os
import re
import shutil

# 视频文件所在的目录
video_directory = "D:\单片机\3--手把手教你学51单片机\3--手把手教你学51单片机"

# 获取目录下所有的视频文件名
video_files = [f for f in os.listdir(video_directory) if os.path.isfile(os.path.join(video_directory, f))]

# 创建章节文件夹
chapter_folders = {}
for video_file in video_files:
    match = re.match(r"(\d+\.\d+)\s*--\s*(.*)", video_file)
    if match:
        chapter = match.group(1)
        if chapter not in chapter_folders:
            chapter_folders[chapter] = os.path.join(video_directory, chapter)
            os.makedirs(chapter_folders[chapter], exist_ok=True)

# 将视频文件移动到对应的章节文件夹
for video_file in video_files:
    match = re.match(r"(\d+\.\d+)\s*--\s*(.*)", video_file)
    if match:
        chapter = match.group(1)
        src_path = os.path.join(video_directory, video_file)
        dst_path = os.path.join(chapter_folders[chapter], video_file)
        shutil.move(src_path, dst_path)

print("视频文件已按章节分类到相应文件夹。")
