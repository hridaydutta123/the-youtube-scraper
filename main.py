import os
from scraper.description_downloader import scrape_video_data
from scraper.comments_downloader import comments_extractor

description_dir = 'data/description'
comments_dir = 'data/comments'

youtube_id = 'W4PaR2oAv6U'
# Get video description
description_response = scrape_video_data(youtube_id)

# Get video comments
comment_response = comments_extractor(youtube_id)

with open(os.path.join(description_dir, youtube_id),'w') as fw:
	fw.write(str(description_response))

with open(os.path.join(comments_dir, youtube_id),'w') as fw:
	fw.write(str(comment_response))

