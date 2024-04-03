import requests
from bs4 import BeautifulSoup
import json
import os

def extract_lyrics_from_html(html_file):

    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    lyrics_elements = soup.find_all('pre')

    lyrics = '\n'.join(lyric.get_text().strip() for lyric in lyrics_elements)
    return lyrics

def process_html_file(html_file):

    lyrics = extract_lyrics_from_html(html_file)

    base_filename = os.path.splitext(html_file)[0] 
    json_filename = base_filename + '_kannada.json' 

    data = {
        'lyrics': lyrics
    }

    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

html_dir = 'html_files_kannada'

for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        html_filepath = os.path.join(html_dir, filename)
        process_html_file(html_filepath)
