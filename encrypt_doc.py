#This simple program allows you to encrypt sensitive documents. You need to install PyPDF2 for it to work
#put the file (myFile.pdf) in the same folder, put your password and your output (encrypted) files name then run the code

from PyPDF2 import PdfWriter

writer = PdfWriter()
writer.append("myfile.pdf")
writer.encrypt("my_password")

with open("my_encrypted_file.pdf", "wb") as f:
    f.write()


