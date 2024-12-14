# Curriculum

This is my workspace for creating my **CV**. The purpose of this repository is to write my CV in markdown and transpose it into docx.

## Convert markdown to docx

To convert it into a .docx file, you must: 

Install Pandoc: <https://pandoc.org/installing.html>  
Install Python 3: <https://www.python.org/downloads/>

Add Pandoc to the Path with the following command:  
`$env:PATH += ”;C:\Program Files\Pandoc”`
  
Inside `curriculum/script`, run the following command:  
`python3 .\markdown_converter.py`

After that, a file will be generated in `curriculum/output`

**Notes**: To update the Curriculum, you must move the cv from the `curriculum/output` folder to `curriculum/docs`.
