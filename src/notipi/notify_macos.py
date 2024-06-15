"""Credits to: https://gist.github.com/MarcAlx/f7a51a245c7c0450dbd4f4203b9916e0 for display_notification()
"""

import os
from importlib import resources

def get_sound_file_path():
    # Replace 'notipi.sounds' with the actual package and subpackage where the sound file is located
    package = 'notipi.sounds'
    resource = 'aurora.mp3'
    
    # Using importlib.resources.path to get the path of the sound file
    with resources.path(package, resource) as p:
        sound_file_path = str(p)
        return sound_file_path

def display_notification(message,title=None,subtitle=None,soundname=None):
	"""
		Display an OSX notification with message title an subtitle
		sounds are located in /System/Library/Sounds or ~/Library/Sounds
	"""
	titlePart = ''
	if(not title is None):
		titlePart = 'with title "{0}"'.format(title)
	subtitlePart = ''
	if(not subtitle is None):
		subtitlePart = 'subtitle "{0}"'.format(subtitle)
	soundnamePart = ''
	if(not soundname is None):
		soundnamePart = 'sound name "{0}"'.format(soundname)

	appleScriptNotification = 'display notification "{0}" {1} {2} {3}'.format(message,titlePart,subtitlePart,soundnamePart)
	os.system("osascript -e '{0}'".format(appleScriptNotification))

	sound_file_path = get_sound_file_path()
	os.system("afplay '{0}'".format(sound_file_path))

if __name__ == '__main__':
	display_notification("Message", title=None, subtitle="Subtitle")