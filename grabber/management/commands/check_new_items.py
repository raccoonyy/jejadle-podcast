# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from grabber.models import Grabber
import time, datetime

class Command(BaseCommand):
    help = '새 설교를 찾아 입력합니다.'

    def handle(self, *args, **options):
        self.stdout.write('\n스크랩 시작 시각: %s\n' % str(datetime.datetime.now()))
        g= Grabber()
        if g.get_sermons():
            self.stdout.write('\n새로운 설교가 입력되었습니다.\n')
        else:
            self.stdout.write('\n새로운 설교가 없습니다.\n')