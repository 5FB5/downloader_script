import requests #lib for working with network
import io       #lib for correctly working with files
import os       #lib for working with os features

file_name = "msg.txt" #name of file with links

files_filter_links = []
files_filtered = []

files_png = [] #initialize arrays with filtered links
files_jpg = []

os.mkdir('downloaded') #create folder with result

with io.open(file_name, encoding='utf-8') as file_src: #transfer messages file to file_src list
    array_buf = [row.rstrip() for row in file_src]

for i in array_buf:
   index_jpg = i.find('.jpg') #try to find interesting extention of file
   index_png = i.find('.png')

   if index_jpg != -1: #if we found extention
       files_filter_links.append(i) #transfer this link into independent array

   if index_png != -1:
       files_filter_links.append(i)

index_jpg = 0 #clear our temp variables
index_png = 0
array_buf = 0

#write data in links_filtered.txt
with io.open('links_filtered.txt', 'w') as file_filtered:
   for i in files_filter_links:
      file_filtered.write(i + '\n')

#open filtered file and write data in temp buff
with io.open('links_filtered.txt', 'r') as file_filtered:
   array_buf = [row.rstrip() for row in file_filtered]
   

for i in array_buf:
   index_jpg = i.find('.jpg')
   index_png = i.find('.png')

   if index_jpg != -1: #if we found extention
       files_jpg.append(i) #transfer this link into independent array

   if index_png != -1:
       files_png.append(i)

for i in files_jpg: #download files in custom folder
   r = requests.get(i)
   with open('downloaded/' + str(files_jpg.index(i)) + '.jpg', 'wb') as pic:
      print('Downloading ' + i + ' ...\n')
      pic.write(r.content)
      pic.close()

for i in files_png:
   r = requests.get(i)
   with open('downloaded/' + str(files_png.index(i)) + '.png', 'wb') as pic2:
      print('Downloading ' + i + ' ...\n')
      pic2.write(r.content)
      pic2.close()

print('Files downloaded!')
