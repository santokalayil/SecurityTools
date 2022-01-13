
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS

class ForensicImage:
    '''This class accepts image url as parameter and provies with number of forensic utilities on it'''
    def __init__(self, file_url):
        self.__image = Image.open(file_url)
    
    @property
    def Image(self):
        '''Returns the PIL Image Object'''
        return self.__image

    def to_numpy_array(self):
        "Returns numpy array of the Image Data for further processing"
        import numpy as np
        return np.array(self.__image.getdata())

    def get_exif_data(self) -> dict :
        '''Returns the all exif meta data of the original image as python dictionary'''
        exif_info_v1 = {TAGS.get(key): value for key, value in self.__image._getexif().items()}
        exif_info_v2 = {key: value if key != "GPSInfo" else {GPSTAGS.get(k): v for k, v in value.items()} for key, value in exif_info_v1.items()}
        return exif_info_v2


    def save_image_without_exif_data(self, output_url):
        '''saves the image's data to a output image url without no exif data info'''
        clean_img = Image.new(self.__image.mode, self.__image.size)
        clean_img.putdata(self.__image.getdata())
        clean_img.save(output_url)


        



