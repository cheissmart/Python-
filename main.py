# # # # # # # # # # # # # # #
#                           #
# Download video from vimeo #
#                           #
# # # # # # # # # # # # # # #

from urllib.request import urlopen
import json

url = "https://player.vimeo.com/video/264406454/config?autopause=1&autoplay=1&byline=0" \
      "&bypass_privacy=1&collections=1&context=Vimeo%5CController%5CChannelController.main" \
      "&default_to_hd=1&outro=nothing&portrait=0&share=1&title=0&watch_trailer=0" \
      "&s=50ee4830f234f014300a0fa57b68e48acf1e5a3d_1526276431"
quality = "720p"
response = urlopen(url)
video_json = json.load(response)

print(video_json)

for video in video_json["request"]["files"]["progressive"]:
    if video["quality"] == quality:
        video_url = video["url"]
        print("Ready for download.")
        print(video_url)
        response = urlopen(video_url)
        print("Downloading...")
        video_file = response.read()
        print("Download complete.")
        file_name = video_url.split('/')[-1]
        f = open(file_name, "wb")
        f.write(video_file)
        f.close()
        break;
