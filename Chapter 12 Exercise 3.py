import urllib.request, urllib.parse, urllib.error

try:
    url = input('Enter URL: ')
    fhand = urllib.request.urlopen(url).read()
    fhand = fhand.decode().strip()
    print (fhand[:3000])
    print(len(fhand))

except:
    print ('url is invalid')
