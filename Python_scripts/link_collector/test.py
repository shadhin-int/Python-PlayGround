import os

# Folder Path
path = '/media/dfs/New Volume/Github/Python-Script/link_collector/File'

# Change the directory
os.chdir(path)



def read_text_file(file_path):
	with open(file_path, 'r') as f:
		print(f.read())


for file in os.listdir():
	if file.endswith(".txt"):
		file_path = f"{path}/{file}"
		is_file_update = os.path.getmtime(file)
		read_text_file(file_path)
