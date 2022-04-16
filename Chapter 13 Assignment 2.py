import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

if True:
    url = input('Enter location: ')
    html = urllib.request.urlopen(url).read()
    html = html.decode().strip()

    info = json.loads(html)   
    print('Retrieving', url)
    print('Retrieved', len(html), 'characters')

    lst = list(info.values())[1]

    count = 0 
    for item in lst:
        count = count + 1
    print('Count:', count)

    total = 0
    for item in lst:
        num = int(item['count'])
        total = total + num
    print('Sum:', total)

    
