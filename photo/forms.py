from django.forms import inlineformset_factory
from .models import *

PhotoInlineFormSet = inlineformset_factory(Album, 
                                           Photo, 
                                           fields = ['image', 'title', 'year','description'], 
                                           extra=2
                                           )