import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

if True:
    url = input('Enter location: ')
    html = urllib.request.urlopen(url).read()
    html = html.decode().strip()

    tree = ET.fromstring(html)
    lst = tree.findall('.//count')
    
    print('Retrieving', url)
    print('Retrieving', len(html), 'characters')
    print('Count:', len(lst))

    total = 0
    for item in tree.findall('.//comment'):
        count = int(item.find('count').text)
        total = total + count

    print('Sum:', total)
    
