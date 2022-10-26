from django.shortcuts import render
import requests
from django.views.generic import *
import json


# Create your views here.
class movieAPI_TV(TemplateView):
    template_name = 'boxoffice.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.core.exceptions import ImproperlyConfigured
        import os
        from pathlib import Path
        BASE_DIR = Path(__file__).resolve().parent.parent
        
        secret_file = os.path.join(BASE_DIR, 'secrets.json')

        with open(secret_file) as f:
            secrets = json.loads(f.read())

        def get_secret(setting, secrets=secrets):
            try:
                return secrets[setting]
            except KeyError:
                error_msg = "Set the {} environment variable".format(setting)
                raise ImproperlyConfigured(error_msg)

        key = get_secret("API_KEY")
        date = '20210701'
        url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={}&targetDt={}&weekGb=0'.format(key, date)
        
        response = requests.get(url)
        context['boxOfficeResult'] = response.json()['boxOfficeResult']

        return context