from requests import get
from requests.exceptions import RequestException
from contextlib import closing


class WebReader:
    def read_web_content(self, web_url):
        try:
            with closing(get(web_url, stream=True)) as response:
                if (self.validate_response(response)):
                    return response.content
                else:
                    return None

        except RequestException as requestException:
            print("Exception raised while consuming {0} - {1}".format(web_url, str(requestException)))
            return None

    def validate_response(self, response):
        html_type = response.headers['Content-Type']
        return (response.status_code == 200
                and html_type is not None
                and html_type.lower().find('html') > -1)
