import urllib.request#url참조
req = urllib.request#req에다가 넣고
d = urllib.request.urlopen("http://forest.skhu.ac.kr/")
status = d.getheaders()
for s in status:
    print(s)