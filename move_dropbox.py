"""Moves Dropbox media files to the appropriate location"""

import media_mover

DROPBOX_FOLDER = 'c:/dev/test/src'
PICTURE_FOLDER = 'c:/dev/test/dest/pics'
VIDEO_FOLDER = 'c:/dev/test/dest/vids'

media_mover.move_pictures(DROPBOX_FOLDER, PICTURE_FOLDER)
media_mover.move_videos(DROPBOX_FOLDER, VIDEO_FOLDER)
