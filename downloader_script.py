import requests #lib for working with network
import io       #lib for correctly working with files
import os       #lib for working with os features
import os.path
import re       #lib for working with regularss

file_name = 'msg.txt' #name of file with links

files_filter_links = []
files_filtered = []

files_pics = []

if not os.path.exists('downloaded'):
    os.mkdir('downloaded') #create folder if not exists

if not os.path.exists(file_name): #create main msg.txt file if not exists
    with io.open(file_name, 'w') as _file:
        _file.write('Put anything to find!')

with io.open(file_name, encoding='utf-8') as file_src: #transfer messages file to file_src list
    array_buf = [row.rstrip() for row in file_src]

#SEARCHING PICTURES
for i in array_buf:
   index_pic_files = re.findall(r'(?i)https://.*\.[j,p][p,n]g', i) #try to find pic's extentions
   if bool(index_pic_files) != False:
       for j in index_pic_files:
           files_filter_links.append(j) #transfer links in filtered array

for i in files_filter_links:
    print(i)

#write data in links_filtered.txt
with io.open('links_filtered.txt', 'w') as file_filtered:
   for i in files_filter_links:
      file_filtered.write(i + '\n')
#END OF SEARCHING PICTURES

array_buf = 0
index_pic_files = []

#open filtered file and write data in temp buff
with io.open('links_filtered.txt', 'r') as file_filtered:
   array_buf = [row.rstrip() for row in file_filtered]
   
for i in array_buf:
   index_pic_files = re.findall(r'(?i)https://.*\.[j,p][p,n]g', i) #try to find pic's extentions
   if bool(index_pic_files) != False:
       for j in index_pic_files:
           files_pics.append(j) #transfer links in filtered array

#TODO: find files's extention for current file's name




#downloading files
# for i in files_pics:
#     net_request = requests.get(i)
#     with open('downloaded/' + str())

#EXAMPLE OF DOWNLOADING
# for i in files_jpg: #download files in custom folder
#    r = requests.get(i)
#    with open('downloaded/' + str(files_jpg.index(i)) + '.jpg', 'wb') as pic:
#       print('Downloading ' + i + ' ...\n')
#       pic.write(r.content)
#       pic.close()

# print('Files downloaded!')
