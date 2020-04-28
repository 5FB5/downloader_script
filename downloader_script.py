import requests #lib for working with network
import io       #lib for correctly working with files
import os       #lib for working with os features
import os.path
import re       #lib for working with regular expressions

file_name = 'msg.txt' #name of file with links

files_filter_links = []

files_links_pics = []

#CREATING FILES
if not os.path.exists('downloaded'):
    os.mkdir('downloaded') #create folder if not exists

if not os.path.exists(file_name): #create main msg.txt file if not exists
    with io.open(file_name, 'w') as _file:
        _file.write('Put anything to find!')

with io.open(file_name, encoding='utf-8') as file_src: #transfer messages file to file_src list
    array_buf = [row.rstrip() for row in file_src]

#SEARCHING LINKS
print('FOUND LINKS:') #Find links via template
for i in array_buf:
   index_links =  re.findall(r'(?i)https://.*\/[^а-яё,\s]*', i) #index_pic_files = re.findall(r'(?i)https://.*\.[j,p][p,n]g', i) 
   if bool(index_links) != False:
       for j in index_links:
           files_filter_links.append(j) #transfer links in filtered array

if files_filter_links:
    for i in files_filter_links:
        print(str(files_filter_links.index(i)) + '. ' + i)
else:
    print('NONE')

#write data in links_filtered.txt
with io.open('links_filtered.txt', 'w') as file_filtered:
   for i in files_filter_links:
      file_filtered.write(i + '\n')

print('\nFOUND LINKS ARE WRITTEN IN LINKS_FILTERED.TXT! DO NOT DELETE IT!\n')
#END OF SEARCHING LINKS

array_buf = []

#open filtered file and write data in temp buff
with io.open('links_filtered.txt', 'r') as links_filtered:
   array_buf = [row.rstrip() for row in links_filtered]

#SEARCHING PICTURES   
for i in array_buf:
   index_pic_files = re.findall(r'(?i)https://.*\.[j,p][p,n]g', i) #try to find pic's extentions (jpg, png)
   if bool(index_pic_files) != False:
       for j in index_pic_files:
           files_links_pics.append(j) #transfer links in filtered array. Now we have all pic's links and work only with it

print('FOUND LINKS TO PICTURES:')
for i in files_links_pics:
    print(str(files_links_pics.index(i)) + '. ' + i)

_file_name = []

#Split links to get file name
for i in files_links_pics:
        current_pic_filename = re.split(r'https://.*\/', i)
        _file_name.append(current_pic_filename[+1])


#DOWNLOADING FILES
#downloading pictures
for i in range(len(files_links_pics)):
    net_request = requests.get(files_links_pics[i])
    if not os.path.exists('downloaded/' + _file_name[i]):
        with io.open('downloaded/' + _file_name[i], 'wb') as current_file_download:
            print('\nDownloading ' + _file_name[i] + '...')
            current_file_download.write(net_request.content)
            print('Downloaded and saved!')
    else:
        with io.open('downloaded/' + str(i) + _file_name[i], 'wb') as current_file_download:
            print('\nDownloading ' + _file_name[i] + '...')
            current_file_download.write(net_request.content)
            print('Downloaded and saved!')

print('\n')
print('\nAll files downloaded and saved in "Downloaded" folder!')