from urllib.parse import urlparse

"""
    This function takes Url and split in into query parameters
    index[0] = 'first query parameter'
    index[1] = 'second query parameter'
"""
def page_url(index, url):
    url_split = urlparse(url)
    dir = url_split.query.strip('&').split('&')
    return dir[index].split('=')[1]

