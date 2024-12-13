import subprocess
from datetime import datetime
import os

markdownfiles = [md for md in os.listdir('../markdown') if md.endswith(".md")]

for file in markdownfiles:
    
    content = file.replace('.md', '_' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    command = f'pandoc "../markdown/{file}" -o "../output/{content}.docx"'
    
    subprocess.run(command)
    
