import requests
from bs4 import BeautifulSoup

class linktr():
    def __init__(self, name) -> None:
        self.baseName = name
        # Get page
        try: self.page = self.getPage()
        except Exception as e: raise f"[-] Request error to: https://linktr.ee/{self.name}\n{e}"
        # Get link on page
        try: self.link = self.getLink()
        except Exception as e:
            self.link = None
            print(f'[!] Could not recover all links\n{e}')
        # get avatar of profil
        try: self.avatar = self.getAvatar()
        except Exception as e:
            self.avatar = None
            print(f'[!] Could not recover avatar\n{e}')
        # Get name of page
        try: self.name = self.getName()
        except Exception as e: 
            self.name = None
            print(f'[!] Could not recover name\n{e}')
        # Get description on page
        try: self.desc = self.getDesc()
        except Exception as e:
            self.desc = None
            print(f'[!] Could not recover description\n{e}')
        # Get social media on page
        try: self.socialMedia = self.getSocialMedia()
        except Exception as e:
            self.socialMedia = None
            print(f'[!] Could not recover social media\n{e}')

    def __str__(self) -> str:
        res = f"""\n{'='*50}\nSearch name: {self.baseName}\nName on site: {self.name}\nAvatar: {self.avatar}\nDescription: {self.desc}\nSocial media:"""
        for i in self.socialMedia.keys():
            res += f"\n    {i}: {self.socialMedia[i]}"
        res += "\nLink:"
        for i in self.link.keys():
            res += f"\n    {i}: {self.link[i]}"
        res += f"\n{'='*50}"
        return res

    def getPage(self):
        res = requests.get(f"https://linktr.ee/{self.baseName}").content.decode('utf8')
        return BeautifulSoup(res, features="lxml")

    def getLink(self):
        linkDict = {}
        res = self.page.find("div", class_="sc-bdfBwQ jrDHLp")
        for elm in res.find_all('div'):
            try:
                elm = elm.find('a')
                linkDict[elm.find('p').text] = elm['href']
            except: pass
        return linkDict

    def getAvatar(self):
        res = self.page.find("div", class_="sc-bdfBwQ sc-gsTCUz dTcluo bhdLno")
        return res.find('img')["src"]

    def getName(self):
        res = self.page.find("div", class_="sc-bdfBwQ sc-gsTCUz dTcluo bhdLno")
        return res.find('h1').text

    def getDesc(self):
        res = self.page.find("div", class_="sc-bdfBwQ sc-gsTCUz dTcluo bhdLno")
        return res.find('h2').text

    def getSocialMedia(self):
        linkDict = {}
        res = self.page.find("div", class_="sc-bdfBwQ sc-gsTCUz cUWRuD bhdLno")
        for elm in res.find_all('a'):
            linkDict[elm['aria-label']] = elm['href']
        return linkDict
