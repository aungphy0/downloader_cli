# downloader cli
$ downloader -h

usage: downloader [-h] url nthreads

## usage: $ downloader www.link.com/file.pdf 3
   - downloader (command)
   - www.link.com (url)
   - 3 (nthreads)

## Set up
   - to test the program linux/unix environment is needed
   - use git command to clone the repo
   - please install python3 on the machine to test the program
     (skip if you already have it)
   - install pip3 from terminal    [sudo apt-get install python3-pip]
   - get the progress module with command [pip3 install progress]
   - after go to .bash_profile with command [nano ~/.bash_profile]
   - use the down arrow key to go to the last line
   - and then make alias by typing -> alias downloader = 'python3 downloader.py'
   - after press control + x and then y and then enter
   - now you can run the downloader command with the following test url  
   - downloaded file will be in the downloader_cli directory

Test URL:<br/>
http://www.titikshapublicschool.com/wp-content/uploads/2018/11/developer-api.jpg<br/>
https://www.bccls.org/BookClubBooks/Alchemist.pdf<br/>
http://jeffe.cs.illinois.edu/teaching/algorithms/book/Algorithms-JeffE.pdf

## Implementation Summary

    When the downloader is running parse_arguments() method get called and return the value from the command <br/>linearguments which are the url and the threads number.

    And then it call the download_file() method <br/>by passing the value of the url and threads.

    In the download_file() method if the connection is okay <br/>then the program get the file name from the url to open the file to later write into it with the <br/>threads.

    After that the program created the threads objects according to the arguments of nthreads, and <br/>each threads call the download() function to download the portion of the bytes from url by each <br/>threads and then it writes into the file which the program created earlier.

    After the download got all <br/>the portions of the bytes, the program call thread join() to terminate each threads and the download <br/>is finished.
