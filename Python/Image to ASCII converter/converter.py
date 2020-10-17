from PIL import Image

dot_char = [' ', '.']

def convert(imagefile, new_width=100, threshold=100):
  """
  Takes imagefile [path to an image] and returns ASCII version of the image
  Optional Parameters:
    + new_width -> width of the ascii version [Note: smaller width causes image to lose details]
    + threshold -> value for which the pixel should be converted into a '.' or ' ' [must lie b/w 0 & 255]
  """
	image = Image.open(imagefile)
	width, height = image.size
	ratio = width/height
	new_height = int(new_width * ratio)
	image = image.resize((new_width, new_height))

	image = image.convert('L')  # converting image to grayscale
	pixels = image.getdata()  # getting data of pixels in the grayscaled image
	characters = "".join([' ' if pixel < threshold else '.' for pixel in pixels])

	pixel_count = len(characters)
	ascii_image = "\n".join([characters[index:index+new_width] for index in range(0, pixel_count, new_width)])
	return ascii_image
