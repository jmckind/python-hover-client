import requests

class HoverException(Exception):
    pass

class HoverAPI(object):
    def __init__(self, username, password):
        params = {"username": username, "password": password}
        r = requests.post("https://www.hover.com/api/login", params=params)
        print r.text

        if not r.ok or "hoverauth" not in r.cookies:
            raise HoverException(r)

        self.cookies = {"hoverauth": r.cookies["hoverauth"]}

    def call(self, method, resource, data=None):
        url = "https://www.hover.com/api/{0}".format(resource)
        r = requests.request(method, url, data=data, cookies=self.cookies)

        if not r.ok:
            raise HoverException(r)
        if r.content:
            body = r.json()
            if "succeeded" not in body or body["succeeded"] is not True:
                raise HoverException(body)
            return body
