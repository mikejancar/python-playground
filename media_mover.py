"""MediaMover"""

import fnmatch
import logging
import os
import shutil
import datetime
import image_info

def move_pictures(src_path, dest_path):
  """Moves image files from a source to a destination"""

  logging.basicConfig(filename='/logs/move-pictures.log', level=logging.INFO,
                      format='%(asctime)s %(message)s', filemode='w')
  logging.info('Moving pictures...')
  picture_ext = '*.jpg'

  pictures_moved = 0

  for media_file in os.listdir(src_path):
    src_file = os.path.join(src_path, media_file)

    if fnmatch.fnmatch(media_file, picture_ext):
      try:
        year_taken = image_info.get_year_taken(src_file)
        dest_dir = os.path.join(dest_path, year_taken)

        move_file(dest_dir, src_file, media_file)
        pictures_moved += 1
      except KeyError:
        logging.error('Could not determine the year %s was taken', src_file)
      except TypeError:
        logging.error('Encountered a non-standard file type for %s', src_file)

  logging.info('Moved %s pictures...', pictures_moved)
  logging.info('------------------------')

def move_videos(src_path, dest_path):
  """Moves video files from a source to a destination"""

  video_ext = '*.mov'

  for media_file in os.listdir(src_path):
    src_file = os.path.join(src_path, media_file)

    if fnmatch.fnmatch(media_file, video_ext):
      raw_time_taken = os.path.getmtime(src_file)
      year_taken = datetime.date.fromtimestamp(raw_time_taken).strftime('%Y')
      dest_dir = os.path.join(dest_path, year_taken)

      move_file(dest_dir, src_file, media_file)

def move_file(dest_dir, src_file, dest_file):
  """Moves a file"""

  if not os.access(dest_dir, os.F_OK):
    os.mkdir(dest_dir)

  full_dest = os.path.join(dest_dir, dest_file)
  shutil.move(src_file, full_dest)
  print 'Moved %s to %s' % (src_file, full_dest)
