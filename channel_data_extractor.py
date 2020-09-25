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
		with open(str(channel_id) + '.json', 'w') as fp:
    		json.dump(yt_channel_dict, fp)
		# Insert into mongo
		# coll.insert(yt_channel_dict)
		

if __name__ == '__main__':
	api_key = 'AIzaSyANTSkc_pzSkqf1pDV2C_JJshV2W1gPe7U'
	api = authenticate(api_key)
	
	with open('', 'r') as fr:
		content = fr.read().split('\n')
		for vals in content:
			channel_data(api, vals)

