import requests #lib for working with network
import io       #lib for correctly working with files
import os       #lib for working with os features
import os.path
import re       #lib for working with regularss

file_name = 'msg.txt' #name of file with links

files_filter_links = []

files_pics = []

if not os.path.exists('downloaded'):
    os.mkdir('downloaded') #create folder if not exists

if not os.path.exists(file_name): #create main msg.txt file if not exists
    with io.open(file_name, 'w') as _file:
        _file.write('Put anything to find!')

with io.open(file_name, encoding='utf-8') as file_src: #transfer messages file to file_src list
    array_buf = [row.rstrip() for row in file_src]

#SEARCHING PICTURES
print('SEARCHING PICTURES:')
for i in array_buf:
   index_pic_files = re.findall(r'(?i)https://.*\.[j,p][p,n]g', i) #try to find pic's extentions
   if bool(index_pic_files) != False:
       for j in index_pic_files:
           files_filter_links.append(j) #transfer links in filtered array
           print(j)

#write data in links_filtered.txt
with io.open('links_filtered.txt', 'w') as file_filtered:
   for i in files_filter_links:
      file_filtered.write(i + '\n')

print('PICTURES LINKS ARE WRITTEN IN LINKS_FILTERED.TXT\n')
#END OF SEARCHING PICTURES

array_buf = 0
index_pic_files = []

#DOWNLOADING 
#open filtered file and write data in temp buff
with io.open('links_filtered.txt', 'r') as file_filtered:
   array_buf = [row.rstrip() for row in file_filtered]
   
for i in array_buf:
   index_pic_files = re.findall(r'(?i)https://.*\.[j,p][p,n]g', i) #try to find pic's extentions
   if bool(index_pic_files) != False:
       for j in index_pic_files:
           files_pics.append(j) #transfer links in filtered array. Now we have all pic's links and work only with it

#TODO: find file's full name
downloading_files = []
downloading_file_name = []
_file_name = []

for i in files_pics: #move from files_pics -> downloading_files
    downloading_files.append(i)

#now we must split links to get filename
for i in downloading_files:
    index_downloading_file = re.findall(r'(?i)https://.*\.[j,p][p,n]g', i)
    if bool(index_downloading_file) != False:
        downloading_file_name.append(i)

for i in downloading_file_name:
    downloading_file_name = re.split(r'https://.*\/', i) 
    _file_name.append(downloading_file_name[+1]) #and finally we can get file name

#downloading files
# for i in _file_name:
#     with io.open('downloaded/' + i, 'w') as current_file: #FIXME: It must create new file every time
#         for j in files_pics:
#             net_request = requests.get(j)
#             print('Downloading ', i, '...\n')
#             current_file.write(net_request.content)
#             print('File downloaded!')
