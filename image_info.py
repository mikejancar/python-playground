"""Get image metadata"""

from datetime import datetime
import os
import exifread

def get_year_taken(image_path):
  """Get the year an image was taken"""
  image_file = open(image_path, 'rb')
  image_tags = exifread.process_file(image_file)

  if 'EXIF DateTimeOriginal' in image_tags:
      date_taken = datetime.strptime(image_tags['EXIF DateTimeOriginal'].printable,
                                     '%Y:%m:%d %H:%M:%S')
      return date_taken.year
  else:
      full_file_name = os.path.basename(image_path)
      short_file_name = os.path.splitext(full_file_name)[0]
      date_taken = datetime.strptime(short_file_name, '%Y-%m-%d %H.%M.%S')
      return str(date_taken.year)
