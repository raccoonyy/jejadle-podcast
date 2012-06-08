from django.db import models
from bs4 import BeautifulSoup
import urllib2

BASE_URL= "http://www.jejadle.org/board/"
BOARD_URL= "http://www.jejadle.org/board/board.asp?tn=sun_sermon"

class Grabber( models.Model ):
    def url2soup(self, url):
        fp= urllib2.urlopen( url )
        text= fp.read()
        if not '<html>' in text:
            text= '<html><head>' + text

        try:
            if '\xb5' in text:
                soup= BeautifulSoup( text.decode("cp949") )
            return soup
        except UnicodeDecodeError as e:
            soup= BeautifulSoup( text.decode("euc-kr") )
            return soup        
        return soup

    def get_sermons(self):
        soup= self.url2soup( BOARD_URL )
        sermon_soups= soup.find( id="Table3" ).select( 'a[onclick^="Cart"]' )
        sermon_soups.reverse() # sorting sermons at program's first run

        sermons= {}
        pre_count_sermon= Sermon.objects.count()
        for sermon_soup in sermon_soups:
            num= sermon_soup.parent.parent.parent.parent.td.text
            title= sermon_soup.parent.parent.parent.parent()[8].text.encode("utf-8")
            url= sermon_soup.parent()[0]['href']
            script_url= BASE_URL + sermon_soup.parent()[6]['onclick'].split("'")[1]
            scripture= self.get_scripture( script_url )

            if self.is_new_sermon( url ):
                s= Sermon.objects.create(
                    num= num,
                    title= title,
                    url= url,
                    scripture= scripture
                )
                s.save()
        post_count_sermon= Sermon.objects.count()

        if pre_count_sermon < post_count_sermon:
            return True
        else:
            return False

    def is_new_sermon(self, url):
        sermon_urls= [sermon.url for sermon in Sermon.objects.all()]
        if not url in sermon_urls:
            return True
        else:
            return False

    def get_scripture(self, url):
        soup= self.url2soup( url )
        br_tags= soup.find_all("table")[1].find_all("br")

        script= []
        for br in br_tags:
            script.append( br.previous.encode("utf-8") )
        script.append( br.next.encode("utf-8") )

        text= "".join( script )
        return text


class Sermon( models.Model ):
    num= models.IntegerField( blank=False )
    title= models.CharField( max_length= 100, blank=False )
    url = models.CharField( max_length= 200, blank=False )
    scripture = models.TextField( blank= True )

    def __unicode__(self):
        return unicode( "num: %s / title: %s" % ( str( self.num ), self.title ) )