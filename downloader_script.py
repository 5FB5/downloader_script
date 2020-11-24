import requests #lib for working with network
import io       #lib for correctly working with files
import os       #lib for working with os features
import os.path
import re       #lib for working with regular expressions
import sys      #lib for working with cmd args
from termcolor import colored, cprint
from colorama import init 

init()

file_name = "links.txt" #name of file with links

files_filter_links = []
files_links_pics = []
_file_name = []

VERSION = "1.2.0"

def getMultipleValidLinks(links_array):
    #SEARCHING LINKS
    print('Links:') #Find links via template
    for i in links_array:
        index_links = re.findall(r'(?i)(?:http|https)://.*\/[^а-яё,\s]*$', i)

        if bool(index_links) != False:
            for j in index_links:
                files_filter_links.append(j) #transfer links in filtered array

        if files_filter_links: # links output
            for i in files_filter_links:
                print(colored('+ ' + i, 'green'))
        
        else:
            print('NONE')

    pass

def searchPicturesLinks(links_array):
    #SEARCHING PICTURES   
    for i in links_array:
        index_pic_files = re.findall(r'(?i)(?:http|https)://.*\.[j,p][p,n]g*', i) #try to find pic's extentions (jpg, png)
        
        if bool(index_pic_files) != False:
            for j in index_pic_files:
                files_links_pics.append(j) #transfer links in filtered array. Now we have all pic's links and work only with it

    print('Pictures:')
    for i in files_links_pics:
        print(colored('+ ' + i, 'green'))

    #Split links to get file name
    for i in files_links_pics:
        current_pic_filename = re.split(r'(?i)(?:http|https)://.*\/', i)
        _file_name.append(current_pic_filename[+1])

def downloadByLinks(file_name_array, links_array):
    for i in range(len(files_links_pics)):
        net_request = requests.get(files_links_pics[i])
        
        if not os.path.exists('downloaded/' + file_name_array[i]):
            with io.open('downloaded/' + file_name_array[i], 'wb') as current_file_download:
                print(colored('\nDownloading ' + file_name_array[i] + '...', 'yellow'))
                current_file_download.write(net_request.content)
                print('Downloaded and saved!')
        else:
            with io.open('downloaded/' + str(i) + file_name_array[i], 'wb') as current_file_download:
                print(colored('\nDownloading ' + file_name_array[i] + '...', 'yellow'))
                current_file_download.write(net_request.content)
                print(colored('Downloaded and saved!', 'green'))

        print('\n')
        print(colored('\nAll files saved in "downloaded" folder!', 'green'))
    
    pass

def downloadManual(): # TODO: manual downloading
    print("In progress")
    pass

def downloadMultipleFiles():
    if (os.path.isfile(file_name)): # if file exists
        #CREATING FILES
        if not os.path.exists('downloaded'):
            os.mkdir('downloaded') #create folder if not exists
        
        with io.open(file_name, encoding='utf-8') as file_src: #transfer messages file to file_src list
            array_buff = [row.rstrip() for row in file_src]

        getMultipleValidLinks(array_buff)

        #write data in links_filtered.txt
        with io.open('links_filtered.txt', 'w') as file_filtered:
            for i in files_filter_links:
                file_filtered.write(i + '\n')
        #END OF SEARCHING LINKS

        array_buff = []

        #open filtered file and write data in temp buff
        with io.open('links_filtered.txt', 'r') as links_filtered:
            array_buff = [row.rstrip() for row in links_filtered]
        print(colored('\nDo NOT delete links_filtered.txt while downloading!\n', 'yellow'))

        # if we want to download pictures
        searchPicturesLinks(array_buff)
        downloadByLinks(_file_name, files_links_pics)
        
    else:
        print(file_name + " doesn't exists!")

    pass

print("\nSimple Python File Downloader")
print("Version: " + VERSION)
print("Made by 5FB5")
print("_______________________________")

while (True):
    mode = input("a - download automatically from " + file_name + " file, m - manual download from link you wrote, q - quit\nCommand: ")

    if (mode == "a"):
        print("\n")
        downloadMultipleFiles()
    
    elif (mode == "m"):
        print("\n")
        downloadManual()

    elif (mode == "q"):
        print("Quitting program...")
        sys.exit(0)