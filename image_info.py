"""Get image metadata"""

from PIL import Image

DATETIME_TAKEN = 36867

def get_year_taken(image_path):
  """Get the year an image was taken"""
  image_taken_at = Image.open(image_path)._getexif()[DATETIME_TAKEN]
  return image_taken_at.split(':')[0]
