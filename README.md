## Table of contents
* [Setup](#setup)
* [Usage](#usage)
* [Sources](#sources)


## Setup

To run this you will need selenium, firefox and geckodriver, Beautiful Soup and lxml.   

You can get geckodriver here: https://github.com/mozilla/geckodriver/releases   
Download release for your operating system, unpack it and move it somewhere where it can be easily added to your path.

I've included python packages and their current version as of writing this in requirements.txt file. You can install them via the file:
```
pip install -r requirements.txt
```
for current user
```
pip install -r requirements.txt --user
```
Or use your preferred way to install them.
   
   
## Usage   
   
Run "yt_playlist_into_txt.py", it will ask which playlist id you want to use, click i agree button and then begin rolling throught the list.   
You can adjust number of times it presses end key, with my connection and the playlist size of ~2300 videos it reached the bottom after about 23 presses.   
So default value is set to 30, as then there's a little more room if page doesn't load as fast or something like that.   
This script was intented for fetching and categorizing my own music playlists so it sorts the results into full albums, eps, splits, demos and file with all of the results
and sorted versions of all these files.
   
If you only want playlists videos titles, you can use provided "only_titles.py"   
It will just get all of the video titles, put them in all.txt and sort them into all_sorted.txt file.   
   
While the main scripts categorizing method isn't perfect as it only matches "full album" etc. words, it depends heavily on the videos uploader how they have named the video.   
I might make regex for this in the future to get more accurate results, but for now this is "good enough" for my needs.   
   
   
## Sources
   
geckodriver: https://github.com/mozilla/geckodriver   
selenium: https://github.com/SeleniumHQ/selenium   
Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/, https://www.crummy.com/software/BeautifulSoup/bs4/doc/   
lxml: https://github.com/lxml/lxml, https://lxml.de/
