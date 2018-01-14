"""Moves Dropbox media files to the appropriate location"""

import media_mover

DROPBOX_FOLDER = 'C:/Users/Mikej/Dropbox/Camera Uploads'
PICTURE_FOLDER = 'D:/Pictures'
VIDEO_FOLDER = 'D:/Video/Home Movies'

media_mover.move_pictures(DROPBOX_FOLDER, PICTURE_FOLDER)
media_mover.move_videos(DROPBOX_FOLDER, VIDEO_FOLDER)
