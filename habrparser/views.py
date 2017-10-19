from base64 import b64encode
from django.http import HttpResponse
from django.views.generic import FormView
from bs4 import BeautifulSoup as bs
import requests

from .forms import ParserForm


class Parser(FormView):
    template_name = 'main/index.html'
    form_class = ParserForm

    def form_invalid(self, form, **kwargs):
        return self.render_to_response({'form': self.get_form()})

    def form_valid(self, form, **kwargs):
        try:
            r = requests.get(form.cleaned_data['url'])
            if r.status_code != 200:
                return HttpResponse('Ошибка, статус не 200')
        except Exception as e:
            return HttpResponse('Ошибка, {error}'.format(error=e))

        soup = bs(r.text, 'html.parser')
        post = soup.find('div', class_='post__body post__body_full')

        src = "data:image/jpeg;base64,%s" % b64encode(form.cleaned_data['file'].file.read()).decode()
        post.select_one('img')['src'] = src
        return HttpResponse(soup.prettify())
