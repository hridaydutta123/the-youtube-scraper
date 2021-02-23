from urllib.request import urlopen

# from apistar import App, Route, types, validators, http
from bs4 import BeautifulSoup
import json
import re

VERSION = '0.1.0'

RESPONSE = {
    'id': str,
    'title': str,
    'upload_date': str,
    'duration': str,
    'description': str,
    'genre': str,
    'is_paid': bool,
    'is_unlisted': bool,
    'is_family_friendly': bool,
    'uploader': {
        'channel_id': str,
    },
    'statistics': {
        'views': int,
        'likes': int,
        'dislikes': int
    }
}


def is_true(string):
    return string.lower() not in ['false', '0']


def remove_comma(string):
    return ''.join(string.split(','))


def make_soup(url):
    '''
    Reads the contents at the given URL and returns a Python object based on
    the structure of the contents (HTML).
    '''
    html = urlopen(url).read()
    return BeautifulSoup(html, 'lxml')


def scrape_video_data(id):
    '''
    Scrapes data from the YouTube video's page whose ID is passed in the URL,
    and returns a JSON object as a response.
    '''

    youtube_video_url = 'https://www.youtube.com/watch?v=' + id


    soup = make_soup(youtube_video_url)
    soup_itemprop = soup.find(id='watch7-content')

    if len(soup_itemprop.contents) > 1:
        video = RESPONSE
        uploader = video['uploader']
        statistics = video['statistics']
        video['regionsAllowed'] = []

        video['id'] = id
        # get data from tags having `itemprop` attribute
        for tag in soup_itemprop.find_all(itemprop=True, recursive=False):
            key = tag['itemprop']
            if key == 'name':
                # get video's title
                video['title'] = tag['content']
            elif key == 'duration':
                # get video's duration
                video['duration'] = tag['content']
            elif key == 'datePublished':
                # get video's upload date
                video['upload_date'] = tag['content']
            elif key == 'genre':
                # get video's genre (category)
                video['genre'] = tag['content']
            elif key == 'paid':
                # is the video paid?
                video['is_paid'] = is_true(tag['content'])
            elif key == 'unlisted':
                # is the video unlisted?
                video['is_unlisted'] = is_true(tag['content'])
            elif key == 'isFamilyFriendly':
                # is the video family friendly?
                video['is_family_friendly'] = is_true(tag['content'])
            elif key == 'thumbnailUrl':
                # get video thumbnail URL
                video['thumbnail_url'] = tag['href']
            elif key == 'interactionCount':
                # get video's views
                statistics['views'] = int(tag['content'])
            elif key == 'channelId':
                # get uploader's channel ID
                uploader['channel_id'] = tag['content']
            elif key == 'description':
                video['description'] = tag['content']
            elif key == 'playerType':
                video['playerType'] = tag['content']
            elif key == 'regionsAllowed':
                video['regionsAllowed'].extend(tag['content'].split(','))

        all_scripts = soup.find_all('script')
        for i in range(len(all_scripts)):
            try :
                if 'ytInitialData' in all_scripts[i].string:
                    match = re.findall("label(.*)",re.findall("LIKE(.*?)like",all_scripts[i].string)[0])[0]
                    hasil = (''.join(match.split(',')).split("\"")[-1]).strip()
                    try:
                        video['statistics']['likes'] = eval(hasil)
                    except:
                        video['statistics']['likes'] = 0
                
                    match = re.findall("label(.*)",re.findall("DISLIKE(.*?)dislike",all_scripts[i].string)[0])[0]
                    hasil = (''.join(match.split(',')).split("\"")[-1]).strip()
                    try:
                        video['statistics']['dislikes'] = eval(hasil)
                    except:
                        video['statistics']['dislikes'] = 0
                
            except :
                pass

        return RESPONSE

    return ({
        'error': 'Video with the ID {} does not exist'.format(id)
    })