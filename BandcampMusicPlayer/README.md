# BandCamp Music Player
This script is associated with automation of storing our play history of tracks from [https://bandcamp.com/](https://bandcamp.com/) in a csv file.
### Note:
The structure of the web pages keep changing frequently. The following code correctly works as of the date: 24 March,2020.

### To run:
- First install a selenium supported webdriver. I have used a Firefox WebDriver, called geckodriver, on a Linux machine:
1. First download the binary of geckodriver from [this](https://github.com/mozilla/geckodriver/releases) site.
2. Copy the extracted binary to /usr/local/bin
- Install selenium: (Recommended to use a virtual environment)
```
pip3 install selenium
```
- Create a csv file in which you want to store the history of tracks heard by you. In my case, I created MyHistory.csv.
- Go to the folder containing the file BandCamp.py, open any console on which you can run python and play around with the following examples:
```python
>>> from BandCamp import BandLeader
>>> b = BandLeader('MyHistory.csv')
>>> b.play()          # should start playing a track
>>> b.play(3)         # plays the third track in the listing
>>> b.play_next()     # plays the next track
>>> b.more_tracks()   # see more music to listen to
>>> b.browser.quit()  # close the webdriver instance. (Note: It is important to do this step while ending the script.)
```
