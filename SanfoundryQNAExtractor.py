def url_pattern(start):
    site=start
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    req = urllib.request.Request(site, headers=hdr)
    google=urllib.request.urlopen(req).read()
    return BeautifulSoup(google,"html.parser")
# tags=soup("p")
def get_url(h):
    san_urls=list()
    y=False
    for i in h:
        store=str(i.get('href'))
        if site==store:
            y=True
        if(y):
            san_urls.append(store)
            if(store==last):
                break
    return san_urls
def Get_The_Text(san_urls,filename):
    # print(san_urls)
    for urls in san_urls:
        count=0
        t=url_pattern(urls)
        for i in t.find_all('p'):
            a=i.get_text()
            # for i in a:
            #     print(i.encode().decode('ascii', 'ignore'))
            filename.writelines(a.encode().decode('ascii', 'ignore'))
            print(a.encode().decode('ascii', 'ignore'))
            if(count==1):
                break
            count+=1
if __name__=="__main__":
    import urllib.request,urllib.parse,urllib.error
    from bs4 import BeautifulSoup
    import random
    import os
    os.chdir(r'C:\Users\Dell\Desktop\Second year college\Scrapping Mandali\SanCG')
    # val=random.randint(1,1000)
    # if not os.path.exists('math'+str(store)):
    #     fil=open(f'C:\Users\Dell\Desktop\Second year college\Scrapping Mandali\math{store}','w')
    # fil=
    # site= "https://www.sanfoundry.com/discrete-mathematics-questions-answers-diagraph/"
    site=input('Enter the starting site : ')
    last=input('Enter the last site : ')
    name_file=input('Enter the name of file')
    if(not os.path.exists(name_file)):
        file=open(f'{name_file}.txt','w')
        token=url_pattern(site)
        va=token('a')
        # for i in va:
        #     print(i.get('href'))
        list_of_urls=get_url(va)
        Get_The_Text(list_of_urls,file)
        file.close()
    else:
        print(f'Delete previous {name_file} file')
    os.chdir(r'C:\Users\Dell\Desktop\Second year college\Scrapping Mandali')
# print(tags)


