import requests
import sys
from xml.etree import ElementTree

def get_podcast_rss_url():
	return sys.argv[1]

def create_request(url):
	server_response = requests.get(url)
	if server_response.status_code != 200:
		print("ERROR: {}".format(server_response.status_code))
		sys.exit(1)
	else:
		return server_response

def get_all_episode_elements_from_xml(xml_text):
	xml = ElementTree.fromstring(xml_text)
	items = xml.findall('channel/item')
    	return items

def download(episode):
	url = episode.find('enclosure').attrib.get('url')
	title = episode.find('title').text
	name = url.split('/')[-1]
	server_response = requests.get(url, stream=True)
	with open(name, 'wb') as fout:
		for chunk in server_response.iter_content(1024*32):
			fout.write(chunk)

def main():
    	rss_url = sys.argv[1]
    	server_response = create_request(rss_url)
    	xml_text = server_response.text
    	items = get_all_episode_elements_from_xml(xml_text)
    	print("Downloading {} episodes...".format(len(items)))
    	episode_count = 1
    	for item in items:
    		download(item)
    		print('Episode',episode_count,'Done.\n')

if __name__ == '__main__':
    	main()
