# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from grabber.models import *


BEFORE_RSS = unicode("""<?xml version="1.0" encoding="utf-8"?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:itunes="http://www.itunes.com/DTDs/Podcast-1.0.dtd" version="2.0">
<channel>
<title>제자들교회 설교 팟캐스트</title>
<itunes:author>제자들</itunes:author>
<link>http://www.jejadle.org/</link>
<description>제자들교회 설교 팟캐스트입니다. 아직까지는 금요예배 설교만 제공됩니다.</description>
<itunes:subtitle>제자들교회 설교 팟캐스트입니다. 아직까지는 금요예배 설교만 제공됩니다.</itunes:subtitle>
<language>ko</language>
<copyright>copyright</copyright>
<itunes:owner>
<itunes:name>raccoony</itunes:name>
<itunes:email>raccoonyy@gmail.com</itunes:email>
</itunes:owner>
<itunes:image href="http://jejadle-podcast.appspot.com/img/jejadle.png" />
""", "utf-8")

AFTER_RSS = unicode("""
</channel>
</rss>
""", "utf-8")

ITEM_RSS = unicode("""
<item>
<title>%s</title>
<itunes:author>제자들</itunes:author>
<description>%s</description>
<itunes:subtitle>%s</itunes:subtitle>
<enclosure url="%s" type="audio/mpeg" />
<guid>%s</guid>
<itunes:category text="Christianity">
</itunes:category>
</item>""", "utf-8")


def main_page(request):
    return render( request, 'main.html' )

def print_rss(request):
    sermons= Sermon.objects.order_by('-id')

    items= ""
    for sermon in sermons:
        items+= ITEM_RSS % ( sermon.title, sermon.scripture, sermon.title, sermon.url, sermon.url)

    rss= BEFORE_RSS + items + AFTER_RSS
    return HttpResponse( rss, content_type="text/xml" )

def check_new_item(request):
    g= Grabber()
    text=''
    if g.get_sermons():
        text= "새 설교가 등록되었습니다."
    else:
        text= "새로운 설교가 없습니다."
    return render( request, 'rss.html', {'text': text} )