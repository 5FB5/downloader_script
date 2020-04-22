import requests #lib for working with network

file_name = "links_file.txt" #name of file with links

files_png = [] #initialize arrays with filtered links
files_jpg = []

with open(file_name) as file_src: #transfer links to array
    array_buf = [row.rstrip() for row in file_src]

for i in array_buf:
   index_jpg = i.find(".jpg") #try to find interesting extention of file
   index_png = i.find(".png")

   if index_jpg != -1: #if we found extention
       files_jpg.append(i) #transfer this link into independent array

   if index_png != -1:
       files_png.append(i)

for i in files_jpg: #download files in custom folder
   r = requests.get(i)
   with open('downloaded/' + str(files_jpg.index(i)) + '.jpg', 'wb') as pic:
      pic.write(r.content)
      pic.close()

for i in files_png:
   r = requests.get(i)
   with open('downloaded/' + str(files_png.index(i)) + '.png', 'wb') as pic2:
      pic2.write(_r.content)
      pic2.close()



