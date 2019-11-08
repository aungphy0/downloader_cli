# downloader cli
$ downloader -h

usage: downloader [-h] url nthreads

positional arguments:
  url         URL of source file to download!
  nthreads    number of threads to download concurrently! Maximum threads can
              put is 10

optional arguments:
  -h, --help  show this help message and exit

## usage: $ downloader www.link.com/file.pdf 3
   - downloader (command)
   - www.link.com (url)
   - 3 (nthreads)

## Set up
   - to test the program linux/unix environment is needed
   - please install python3 on the machine to test the program
     (skip if you already have it)
   - install pip3 from terminal (sudo apt-get install python3-pip)
   - get the progress module with command (pip3 install progress)
   -
