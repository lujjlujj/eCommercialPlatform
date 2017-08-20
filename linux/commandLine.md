#Command Line

##Generate heapdump
sudo /sys1/proclib/stdbuild/bpm80/heapdump.sh [processId]

##Generate Java Core
kill -3

##Find Keyword in System File
find /f -exec grep -H "TMOUT" {} \; | less;

##Grep response time from access.log
less access_log.secure.xxxxx | awk '$20 !~/xsd$/'| awk '$20>2000000' | less
less access_log.secure.xxxxx | awk '$20 !~/xsd$/'| awk '$20>2000000' | less | wc -l

##Find File & Folder
Find is a very strong command to search for files and folders. You can search for files based on certain criteria besides filename, such as file types, atime, belongs to which groups, file modes, etc. Because find command support a lots of options, therefore sometimes find command line looks very complicated, but actually it is not. Don’t let the lengthy find command lines scares you away, find can be very easy to use.
You just need to ask yourself 3 question?
1. What is the path you want to begin your search from? current directory.
2. What is the filename you want to search? any files with keyword ‘love’
3. What is the file types? normal file
Okay, lets construct the simple find command line.
*find . -name "*love*" -type f
1. Current directory can be write as a single dot (.)
2. Specified the filename by option -name and you can use wildcard to construct your keyword.
3. Use -type to force your file type for accuracy search result, but you can ignore specifying the -type.
( check out -type in man page for more info)
Do you want to know more?
I want to manipulate the result of find. Let say I want to find all wave files in a specific folder, and I want to know the file info of each wave file. Lets construct the find command line:
*find ~/uc/dump -name "*.wav" -exec file {} \;
It start to looks complicated, but it is quite straight forward, -exec means execute, file are the command i use to check the file info, {} indicate the find’s result, \; is something I don’t understand, but have to be there. \; probably are use to separate each find’s result, i guess.
Do you want more? I want to find all my documents with extension .pdf and .chm, how do I construct my find command line.
*find /home/hkong/documents/ -name "*.pdf" -or -name "*.chm"
With using -or, you can specify your more than one keywords as file name. This is very useful, we usually execute find twice for different keywords, actually we can do this in one line.
Do you have any interesting find tips to share with us?

##Execute Command Line in backend
nohup + xxxx + &

##Unzip File
*Here is an example of how to extract the contents of a gzip file
    gzip -d file.gz

*Here is an example of how to extract the contents of a tar file
    tar xvf file.tar

*Here is an example to how to tar the orginal file
    tar cvf target orignal

##Get PC Info
uname -a

##Set Proxy
export http_proxy=http://Username:Password@hostname:port/