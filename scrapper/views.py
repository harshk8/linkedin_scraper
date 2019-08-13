from django.shortcuts import render
from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import requests
from selenium.webdriver.common.keys import Keys
import pprint


from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

class ScrapCompanyInfo(APIView):
    def get(self, request):
        driver = settings.DRIVER
        company_name = request.GET['company']
        driver.get('https://www.linkedin.com/company/'+ company_name + "/about/")
        company = {}

        html = driver.page_source
        soup = BeautifulSoup(html)

        # try:
        #     company['name'] = soup.select_one(".ember-view > h1 > span").getText(strip=True)
        # except:
        #     pass
        # try:
        #     company['overview'] = soup.select_one(".white-space-pre-wrap").getText(strip=True)
        # except:
        #     pass        
        # try:
        #     company['logo'] = soup.select_one(".ember-view > div > div.org-top-card-primary-content__logo-container > img").get_attribute('src')
        # except:
        #     pass   

        # try:
        #     company[soup.select_one(".ember-view > dl > dt:nth-child(1)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(2) a").get_attribute('href')
        # except:
        #     pass

        # try:
        #     company[soup.select_one(".ember-view > dl > dt:nth-child(3)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(4)").getText(strip=True)
        # except:
        #     pass
        # try:
        #     company[soup.select_one(".ember-view > dl > dt:nth-child(5)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(6)").getText(strip=True)
        # except:
        #     pass
        # try:
        #     company[soup.select_one(".ember-view > dl > dt:nth-child(7)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(8)").getText(strip=True)
        # except:
        #     pass
        # try:
        #     company[soup.select_one(".ember-view > dl > dt:nth-child(9)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(10)").getText(strip=True)
        # except:
        #     pass
        # try:
        #     company[soup.select_one(".ember-view > dl > dt:nth-child(11)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(12)").getText(strip=True)
        # except:
        #     pass
        # import pdb; pdb.set_trace()
        try:
            company['name'] = soup.select_one(".org-top-card-summary__title > span").getText(strip=True)
        except:
            pass
        try:
            company['overview'] = soup.select_one(".white-space-pre-wrap").getText(strip=True)
        except:
            pass        
        try:
            company['logo'] = soup.select_one(".org-top-card-primary-content__logo-container > img")['src']
        except:
            pass   
        import pdb; pdb.set_trace()
        try:
            company[soup.select_one(".mb3.container-with-shadow.ember-view >  dl > dt:nth-of-type(1)").getText(strip=True)] = soup.select_one(".mb3.container-with-shadow.ember-view >  dl > dt:nth-of-type(2)").get_attribute('href')
        except:
            pass
        try:
            company[soup.select_one(".mb3.container-with-shadow.ember-view >  dl > dt:nth-of-type(3)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(4)").getText(strip=True)
        except:
            pass
        try:
            company[soup.select_one(".mb3.container-with-shadow.ember-view >  dl > dt:nth-of-type(5)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(6)").getText(strip=True)
        except:
            pass
        try:
            company[soup.select_one(".mb3.container-with-shadow.ember-view >  dl > dt:nth-of-type(7)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(8)").getText(strip=True)
        except:
            pass
        try:
            company[soup.select_one(".ember-view > dl > dt:nth-child(9)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(10)").getText(strip=True)
        except:
            pass
        try:
            company[soup.select_one(".ember-view > dl > dt:nth-child(11)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(12)").getText(strip=True)
        except:
            pass
        try:
            company[soup.select_one(".ember-view > dl > dt:nth-child(13)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(14)").getText(strip=True)
        except:
            pass
        try:
            company[soup.select_one(".ember-view > dl > dt:nth-child(15)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(16)").getText(strip=True)
        except:
            pass
        try:
            company[soup.select_one(".ember-view > dl > dt:nth-child(17)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(18)").getText(strip=True)
        except:
            pass
        try:
            company[soup.select_one(".ember-view > dl > dt:nth-child(19)").getText(strip=True)] = soup.select_one(".ember-view > dl > dd:nth-child(20)").getText(strip=True)
        except:
            pass

        return Response(company)