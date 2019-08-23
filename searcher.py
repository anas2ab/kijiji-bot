from urllib.request import urlopen as uReq
import string
# this url for ref only
# https://www.kijiji.ca/b-search/b-search/iphone-x/k0c760l1700272

url_base = "https://www.kijiji.ca/"
url_category = "b-search/"
url_location = "b-search/"
url_ids = "/k0c760l1700272/"


def url_generator(item, min_price, max_price, page_num):
    """
   This function will return url generated based on search item, min and max price
   :param item:
   :param min_price:
   :param max_price:
   :param page_num:
   :return:
   """

    item_spaced = item.replace(" ", "-")

    url_price = "?price=" + min_price + "__" + max_price
    page = "/page-" + page_num
    url = url_base + url_category + url_location + item_spaced + page + url_ids + url_price

    return url
