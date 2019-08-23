from urllib.request import urlopen as uReq
import string
# this url for ref only
# https://www.kijiji.ca/b-search/b-search/iphone-x/k0c760l1700272

url_base = "https://www.kijiji.ca/"
url_category = "b-search/"
url_location = "b-search/"
url_ids = "/k0c760l1700272/"


def url_generator(item, min_price, max_price):
    """
   This function will return url generated based on search item, min and max price
   :param item:
   :param min_price:
   :param max_price:
   :return:
   """

    item_spaced = item.replace(" ", "-")

    url_price = "?" + min_price + "__" + max_price
    url = url_base + url_category + url_location + item_spaced + url_ids + url_price

    return url
