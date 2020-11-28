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

VERSION = "1.2.0"

def getMultipleValidLinks(links_array):
    #SEARCHING LINKS
    print('Links:') #Find links via template
    for i in links_array:
        index_links = re.findall(r'(?i)(?:http|https)://.*\/[^а-яё,\s]*$', i)

        if bool(index_links) != False:
            for j in index_links:
                files_filter_links.append(j) #transfer links in filtered array
                # getting filename from current link
                current_filename = re.split(r'(?i)(?:http|https)://.*\/', j)
                _file_name.append(current_filename[+1])

        if files_filter_links: # links output
            for i in files_filter_links:
                print(colored('+ ' + i, 'green'))
        
        else:
            print('NONE')

    pass

def downloadByLinks(file_name_array, links_array):
    i = 0
    for i in range(len(links_array)):
        net_request = requests.get(links_array[i])

        if (not os.path.exists('downloaded/'.join(file_name_array[i]))):
            with io.open('downloaded/' + file_name_array[i], 'wb') as current_file_download:
                print(colored('\nDownloading ' + file_name_array[i] + '...', 'yellow'))
                current_file_download.write(net_request.content)
                print('Downloaded and saved!')
        else:
            with io.open('downloaded/' + str(i) + file_name_array[i], 'wb') as current_file_download:
                print(colored('\nDownloading ' + str(i) + file_name_array[i] + '...', 'yellow'))
                current_file_download.write(net_request.content)
                print(colored('Downloaded and saved!', 'green'))

        print('\n')
        print(colored('\nAll files saved in "downloaded" folder!', 'green'))
    
    pass

def downloadByLink(filename, link):
    i = 0
    net_request = requests.get(link)

    if (not os.path.exists('downloaded/'.join(filename))):
        with io.open('downloaded/' + filename, 'wb') as current_file_download:
            print(colored('\nDownloading ' + filename + '...', 'yellow'))
            current_file_download.write(net_request.content)
            print('Downloaded and saved!')
    else:
        with io.open('downloaded/'+ str(i).join(filename), 'wb') as current_file_download:
            print(colored('\nDownloading '.join(str(i)).join(filename) + '...', 'yellow'))
            current_file_download.write(net_request.content)
            print(colored('Downloaded and saved!', 'green'))

    print('\n')
    print(colored('\nAll files saved in "downloaded" folder!', 'green'))

pass

def downloadOnce(_link): # TODO: manual downloading

    fileName = re.split(r'(?i)(?:http|https)://.*\/', _link)
    downloadByLink(fileName, _link)
    
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

        #open filtered file and write data in temp buff
        with io.open('links_filtered.txt', 'r') as links_filtered:
            array_buff = [row.rstrip() for row in links_filtered]
        print(colored('\nDo NOT delete links_filtered.txt while downloading!\n', 'yellow'))

        downloadByLinks(_file_name, files_filter_links)
    
    else:
        print(file_name + " doesn't exists!")
    
    pass

print("\nSimple Python File Downloader")
print("Version: " + VERSION)
print("Made by 5FB5")
print("_______________________________")

while (True):
    array_buff = []
    files_filter_links = []
    files_links_pics = []
    _file_name = []

    mode = input("a - download automatically from " + file_name + " file, m - manual download from link you wrote, q - quit\nCommand: ")

    if (mode == "a"):
        downloadMultipleFiles()

    elif (mode == "m"):
        print("\n")
        current_link = input("Enter link you need: ")
        downloadOnce(current_link)

    elif (mode == "q"):
        print("Quitting program...")
        sys.exit(0)