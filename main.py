import os
import yapi
import argparse
import json
from scraper.description_downloader import scrape_video_data
from scraper.comments_downloader import comments_extractor
from pprint import pprint


parser = argparse.ArgumentParser()
# parser.add_argument('--video_id', required=True, help='YouTube video ID')
parser.add_argument('--out_dir', required=True, help='Directory to store video description')
args = vars(parser.parse_args())

# Create if directory does not exist
if not os.path.exists(args['out_dir']):
    os.makedirs(args['out_dir'])

usersDone = os.listdir('output')
existingUsers = [x[:-5] for x in usersDone]
print(existingUsers)
# with open('yt_ids.txt','r') as fr:
# 	ids = fr.read().split('\n')

# 	for vals in ids:
# 		try:
# 			# Get video description
# 			description_response = scrape_video_data(vals)

# 			# Get video comments
# 			comment_response = comments_extractor(vals)

# 			response = {
# 				'video_description': description_response,
# 				'comment_response': comment_response
# 			}

# 			with open(os.path.join(args['out_dir'],vals + '.json'), 'w') as fw:
# 				fw.write(json.dumps(response))
# 		except:
# 			continue
# # print(json.dumps(response))


