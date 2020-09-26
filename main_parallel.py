import os
import yapi
import argparse
import json
from scraper.description_downloader import scrape_video_data
from scraper.comments_downloader import comments_extractor
from pprint import pprint
import multiprocessing
from joblib import Parallel, delayed
from tqdm import tqdm

num_cores = multiprocessing.cpu_count()
# num_cores = 30
print('Total number of cores: {}'.format(num_cores))


parser = argparse.ArgumentParser()
parser.add_argument('--input_file', required=True, help='Input file name with list of video ids (one video id per line)')
parser.add_argument('--out_dir', required=True, help='Directory to store video description')
args = vars(parser.parse_args())

# Create if directory does not exist
if not os.path.exists(args['out_dir']):
    os.makedirs(args['out_dir'])

def extract_data(ids):
	try:
		# Get video description
		description_response = scrape_video_data(ids)

		# Get video comments
		comment_response = comments_extractor(ids)

		response = {
			'video_description': description_response,
			'comment_response': comment_response
		}

		with open(os.path.join(args['out_dir'],ids + '.json'), 'w') as fw:
			fw.write(json.dumps(response))
	except:
		pass

if __name__ == "__main__":
	with open(args['input_file'],'r') as fr:
		ids = fr.read().split('\n')
	inputs = tqdm(ids)

	processed_list = Parallel(n_jobs=num_cores)(delayed(extract_data)(i) for i in inputs)