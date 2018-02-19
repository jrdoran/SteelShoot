print ("jd starting")

#import BeautifulSoup
from bs4 import BeautifulSoup
#from urllib import urlopen
#from urllib.request import urlopen
#import request
import requests
#import re
#from bs4.tests.test_tree import SiblingTest

hosturl = "https://steelchallenge.com/steel-challenge-Match-Calendar-Home.php"
r=requests.get(hosturl)
data = r.text
soup = BeautifulSoup(data, 'lxml')


taglist = soup.findAll('a') #all "a" tag in a soup list
print ("total anchor elements:  " + str(len(taglist)))


for tag in taglist:
    if tag["href"].startswith("?indx"):
        childurl = hosturl +"/" +tag ["href"]
        print ( "\n"+ childurl)  # here was have one of the detailed links to a competition;


        r=requests.get(childurl)  # go fetch the detailed link;
        data = r.text
        soup = BeautifulSoup(data, 'lxml')


        sublist = soup.findAll('th')   # th is very close;  tr does include data but alot more
        for sub1 in sublist:
                sibling = sub1.find_next_sibling()
                
                print ("aaaaa "+ str(sub1.contents[0]))
                print ("bbbbb "+ str(sibling.contents[0]))
                print()
        
        
        
        #quit()
    # loop end 
# outside of loop; main


'''

if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')



'''



# https://steelchallenge.com/steel-challenge-Match-Calendar-Home.php/?indx=4059

#<h1>SCSA Matches</h1>
#<table border=0>
#<tr><th valign=top align=left>Match Name:</th><td>Strongpoint Steel Challenge February 2018</td></tr>
#<tr><th valign=top align=left>Tier:</th><td>Tier I</td></tr>
#<tr><th valign=top align=left>Date:</th><td>2/10/18 - 2/11/18</td></tr>
#<tr><th valign=top align=left>Club:</th><td>Strong Point Shooting Complex (SCSA249) </td></tr>
#<tr><th valign=top align=left>Location:</th><td>Waverly Hall, Ge</td></tr>
#<tr><th valign=top align=left>Contact:</th><td>Scott Franklin</td></tr>
#<tr><th valign=top align=left>Phone:</th><td>706-573-5726</td></tr>
#<tr><th valign=top align=left>Email:</th><td><a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="7513190c1b06141c1947351218141c195b161a18">[email&#160;protected]</a></td></tr>
#<tr><th valign=top align=left>URL:</th><td>strongpointshooting.com</td></tr>
#<tr><th valign=top align=left>Additional Info:</th><td>Registration starts at 9:00, shooter briefing at 9:30, start shooting at 10:00.</td></tr>
#</table>
#<br><a href="?">Return to match listing</a>


print (" \n jd done ")
#quit()
