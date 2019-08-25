from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "http://feeds.soundcloud.com/users/soundcloud:users:152948051/sounds.rss"

@plugin.route('/')
def main_menu():
    items = [
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "http://i1.sndcdn.com/avatars-000591343872-cyz7bk-original.jpg"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "http://i1.sndcdn.com/avatars-000591343872-cyz7bk-original.jpg"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

if __name__ == '__main__':
    plugin.run()
