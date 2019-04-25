import numpy as np
import pandas as pd
import sys
import yapi
import xml.etree.ElementTree as ET


def authenticate(api_key):
	api = yapi.YoutubeAPI(api_key)
	return api

def channel_data(api, channel_id):
	# channel details
	channel_details = api.get_channel_by_id(channel_id)
	
	# print(channel_details)
	if len(channel_details.items) > 0:
		country = None
		if 'country' in channel_details.items[0].snippet:
			country = channel_details.items[0].snippet.country

		# Parse channel in details
		yt_channel_dict = {
			'channel_id': channel_id,
			'comment_count': int(channel_details.items[0].statistics.commentCount),
			'hiddenSubscriberCount': int(channel_details.items[0].statistics.hiddenSubscriberCount),
			'subscriberCount': int(channel_details.items[0].statistics.subscriberCount),
			'videoCount': int(channel_details.items[0].statistics.videoCount),
			'viewCount': int(channel_details.items[0].statistics.viewCount),
			'country': country,
			'description': channel_details.items[0].snippet.description,
			'title': channel_details.items[0].snippet.title,
			'publishedAt': channel_details.items[0].snippet.publishedAt,
			'kind': channel_details.items[0].kind,
			'etag': str(channel_details.items[0].etag)
		}
		print(yt_channel_dict)
		# Insert into mongo
		# coll.insert(yt_channel_dict)
		

if __name__ == '__main__':
	api_key = '<ENTER-YOUTUBE-API-KEY>'
	api = authenticate(api_key)
	
	# channels = set()
	channel_data(api, 'UCNPDjf7VSFQ1BvQ96yjpAEQ')
	# with open('../data/ylh/yt_subs_follower.csv', 'r') as fr:
	# 	content = fr.read().split('\n')
	# 	for vals in content:
	# 		channel_data(api, eval(vals)[1])

