import random
import urllib.request

url = input("Enter URL ")
# url = "https://she-codes.org/wp-content/uploads/2018/11/cropped-unnamed-1-1.png"


def get_pics(url):
    random_num = random.randint(1, 1000)
    name_of_file = str(random_num) + '.jpg'

    urllib.request.urlretrieve(url, filename=name_of_file)


get_pics(url)
