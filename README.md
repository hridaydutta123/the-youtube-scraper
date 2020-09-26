# the-youtube-scraper
##### Download YouTube video description and video comments without using the YouTube API.

### Setup
(1) You do not need to any API Credentials to use this.

(2) The final output will be stored in a JSON file.

### Clone and use the Python script
```
$ git clone https://github.com/hridaydutta123/the-youtube-scraper.git
$ cd the-youtube-scraper
$ sudo pip install -r requirements.txt
```

### Usage
Finally you can run the script by entering one YouTube video ID and output directory path at the command line:
1. Download video metadata and video comments from a single YouTube video
```
$ python3 main.py --video_id <enter-youtube-video-id> --out_dir <enter-output-directory-path>
```
2. Download video metadata and video comments from a list of YouTube videos parallely (x num of cores times faster) 
```
$ python3 main_parallel.py --input_file <enter-file-name-with-list-of-video-ids(one-video-id-per-line)> --out_dir <enter-output-directory-path>
```

### Output Format
```
{
  "comment_response": [
    {
      "author": "Uday Simha",
      "text": "Vanishing gradient is due to large sequences or dude to more nodes in a layer or due to deep networks?﻿",
      "ensure_ascii": false,
      "cid": "UgyxmBEJrQS0To2Fo5R4AaABAg",
      "time": "1 week ago"
    },
    {
      "author": "Sandeep Kumar",
      "text": "For a 200 channel(bands) satellite image of dimension 145x145 has 16 \nclasses.I have a groundtruth of dimension 145x145 (containing values \nfrom 1 to 16 that represent 16 different classes).I need to perform LSTM\n on a small patch of image (say of dimension 5x5x200) because \nneighboring pixels are similar.Can you tell  me how to give the data to @t mail id is sandeep.Ladi@@t﻿",
      "ensure_ascii": false,
      "cid": "Ugy_5NTrbFIPLzNOtYt4AaABAg",
      "time": "1 month ago"
    },
    {
      "author": "Ömer Yalçın",
      "text": "Hi that is great video , thanks for sharing. You can use \"keras.layers.CuDNNLSTM()\" for uping speed.﻿",
      "ensure_ascii": false,
      "cid": "Ugyc_biVWUJooIhFZWl4AaABAg",
      "time": "3 months ago (edited)"
    },
    {
      "author": "Saravana Kumar",
      "text": "Are you British﻿",
      "ensure_ascii": false,
      "cid": "UgyOC9tQ3SBMfN4G_7F4AaABAg",
      "time": "4 months ago"
    },
    {
      "author": "Machine Learning at Microsoft",
      "text": "Yes!﻿",
      "ensure_ascii": false,
      "cid": "UgyOC9tQ3SBMfN4G_7F4AaABAg.8mwZjbe5R6C8mzrRtq8hwX",
      "time": "4 months ago"
    },
    {
      "author": "Dinesh Mane",
      "text": "Fantastic session Tim, and content is really good. \nYou have explained return_sequence = True parameter with two examples which helped me to understand clearly. \nThanks for sharing the video :)﻿",
      "ensure_ascii": false,
      "cid": "UgyQ1m5GjlpKsKfMg954AaABAg",
      "time": "7 months ago"
    },
    {
      "author": "Tomás Emilio Silva Ebensperger",
      "text": "awesome video sir. i will read the book.﻿",
      "ensure_ascii": false,
      "cid": "UgxyoZk56yUpqiZmxhF4AaABAg",
      "time": "7 months ago"
    }
  ],
  "video_description": {
    "thumbnail_url": "https://i.ytimg.com/vi/ZmCzrPVzDQI/maxresdefault.jpg",
    "uploader": {
      "thumbnail_url": "https://yt3.ggpht.com/a-/AAuE7mBlSX-JPA4rXmz0LhppdTWsCiD8rM9ZjSY9Fg=s48-c-k-c0xffffffff-no-rj-mo",
      "channel_id": "UCXvHuBMbgJw67i5vrMBBobA",
      "is_verified": false,
      "name": "Machine Learning at Microsoft"
    },
    "is_family_friendly": true,
    "genre": "Science & Technology",
    "duration": "PT57M36S",
    "description": "Tim Scarfe takes you on a whirlwind tour of sequence modelling in deep learning using Keras! \n\n• Intro \n•  Outline 2:03\n•  What is a neural network 2:38\n• Concepts of deep learning 3:32\n• What is a sequence? 8:34\n• What is sequence processing? 9:28\n• Tokenization 10:35\n• word vectors vs word embeddings 12:06\n• More about word embeddings 13:26\n• Recurrent neural networks (RNNs) 15:26\n• LSTMs 17:04\n• GRUs vs LSTMs 18:31\n• Bi-directional RNNs 19:28\n• 1d CNNs and tour of convolutional filtering in MATLAB 20:22\n• Stacking RNNs+CNNs 25:42\n• Universal machine learning process 25:56\n• Demo-1 hot encoding 29:17\n• Demo-Defining RNNs in Keras 31:17\n• Demo-IMDB in Keras 32:30\n• Performance/scoring/eval of deep learning models 35:40\n• Question on material and sigmoid activation 38:39\n• Temperature forecasting problem (cover GRU, LSTM, regularisation, bidirectional, stacking) 41:55\n• 1D CNNs 49.49\n• Questions 52:00\n\nSlides; https://github.com/ecsplendid/deep-le...\n\nMake sure you buy yourself a copy of Francois Chollet's book https://www.manning.com/books/deep-le...",
    "title": "Sequence Modelling and NLP With Deep Learning (Keras)",
    "upload_date": "2018-03-04",
    "is_paid": false,
    "id": "ZmCzrPVzDQI",
    "is_unlisted": false,
    "statistics": {
      "dislikes": 2,
      "views": 5118,
      "likes": 105
    }
  }
}
```

### References
[1] https://github.com/egbertbouman/youtube-comment-downloader

[2] https://github.com/faheel/youtube-scraper-api
