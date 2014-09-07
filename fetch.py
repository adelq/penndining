import requests

class DiningAPI(object):
  s = requests.Session()

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def fetch(self):
    return
