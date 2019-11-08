#command line interface using python3
#download file from url with multithread
import requests
import argparse
import threading
import sys
from progress.bar import Bar


def download(start,end,url,filename):

    #define the portion of file to request from url
    headers = {'Range': 'bytes=%d-%d' %(start,end)}
    #get file_name from passing value
    file_name = filename
    #get the response from the url by headers value of bytes
    with requests.get(url, headers=headers, stream=True) as response:
            #open the file_name and read and write bytes to the file
            with open(f'./{file_name}', 'r+b') as file:
                file.seek(start)
                file.write(response.content)


def download_file(parse_url,parse_nthreads):
    url = parse_url
    #if there is no connection or no content-length key in the headers
    #the program will exit
    try:
        file_info = requests.head(url)
        file_size = int(file_info.headers['content-length'])
    except Exception as e:
        print('No connection! or No content-length in the header!')
        print('')
        sys.exit(0)

    #if try is work get the file name from url of the last token
    filename = url.split('/')[-1]
    #create the file for later write into it
    file = open(filename,"wb")
    file.close()
    #split the file size with number of threads used
    parts = int(file_size) / parse_nthreads

    for i in range(parse_nthreads):
        start = int(parts * i)
        end = int(start + parts)
        #create the thread object by calling download function with each portion
        t = threading.Thread(target=download,
                            kwargs={'start':start,'end':end,
                            'url':url,'filename':filename},daemon=True)

        t.start()
    #define the main_thread for later check
    main_thread = threading.main_thread()

    with Bar('Processing',max=parse_nthreads) as bar:
        for t in threading.enumerate():
            #if the thread is not main_thread then join and terminate it
            if t is not main_thread:
                bar.next()
                t.join()


def parse_arguments():
    parser = argparse.ArgumentParser('downloader')

    #command line argument for url
    parser.add_argument('url', type = str, action='store',
                        metavar= 'url', default = None,
                        help = "URL of source file to download!")
    #command line argument for threads
    parser.add_argument('nthreads', type = int, action='store',
                        metavar= 'nthreads', default=1,
                        help = "number of threads to download concurrently!\
                                Maximum threads can put is 10")

    return parser.parse_args()


if __name__ == "__main__":
    print('')
    arguments = parse_arguments()

    #limit the threads number to 10
    if arguments.nthreads > 10:
        print('Maximum threads can be used is 10!')
        sys.exit(0)

    download_file(arguments.url,arguments.nthreads)

    print('Successfully download!')
