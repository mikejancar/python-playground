"""MediaMover"""

import re
import logging
import os
import shutil
import image_info

def move_pictures(src_path, dest_path):
  """Moves image files from a source to a destination"""

  logging.basicConfig(filename='/logs/move-media.log', level=logging.INFO,
                      format='%(asctime)s %(message)s', filemode='w')
  logging.info('Moving pictures...')

  picture_ext_pattern = '.*\.[j|p][p|n]g'
  duplicate_pattern = '.*-[\d]\.[j|p][p|n]g'
  pictures_moved = 0
  duplicates_found = 0

  for media_file in os.listdir(src_path):
    src_file = os.path.join(src_path, media_file)

    if re.match(picture_ext_pattern, media_file):
      if re.match(duplicate_pattern, media_file):
        move_file('C:/temp', src_file, media_file)
        duplicates_found += 1
      else:
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
  logging.info('Found %s duplicates...', duplicates_found)
  logging.info('------------------------')

def move_videos(src_path, dest_path):
  """Moves video files from a source to a destination"""

  video_ext_pattern = '.*\.[m|3|g][p|g|i|o][4|p|f|v]'
  videos_moved = 0

  for media_file in os.listdir(src_path):
    src_file = os.path.join(src_path, media_file)

    if re.match(video_ext_pattern, media_file):
      try:
        year_taken = image_info.get_year_taken(src_file)
        dest_dir = os.path.join(dest_path, year_taken)

        move_file(dest_dir, src_file, media_file)
        videos_moved += 1
      except ValueError:
        logging.error('Encountered an invalid file name for %s', src_file)

  logging.info('Moved %s videos...', videos_moved)
  logging.info('------------------------')

def move_file(dest_dir, src_file, dest_file):
  """Moves a file"""

  if not os.access(dest_dir, os.F_OK):
    os.mkdir(dest_dir)

  full_dest = os.path.join(dest_dir, dest_file)
  shutil.move(src_file, full_dest)
  logging.info('Moved %s to %s', src_file, full_dest)
