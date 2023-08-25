from django.shortcuts import render
import os

# Create your views here.
curdir = os.getcwd()


def index(req):
    return render(req, 'index.html')


def chokolate(req, id):
    id = int(id)
    file = open(curdir + '/chokolates/static/text/content', 'r', encoding='utf-8')
    chokoinfo = list(map(lambda x: list(x.split(' # ')), file.readlines()))
    file.close()
    name, img, text, link, color = chokoinfo[id]
    return render(req, 'choko.html', context={'id': id, 'name': name, 'img': img, 'text': text, 'link': link, 'color': color})
