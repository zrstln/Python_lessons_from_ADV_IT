from urllib import request
import sys

myurl ="https://adv400.tripod.com/lpi-010-150.jpg"
myfile = "D:\\temp\\mypic.jpg"
# myheader = {}
# myheader['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

try:
    print("Start downloading file from url: " + myurl)
    request.urlretrieve(myurl, myfile)
except Exception:
    print("AHTUNG AHTUNG")
    print(sys.exc_info())
    exit()

print("File downloaded saved " + myfile)
