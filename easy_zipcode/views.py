# -*- coding: utf-8 -*-
from django.views.generic import DetailView

from main import EasyZipCode


class EasyZipCodeDetailView(DetailView):
    main_class = EasyZipCode

    def get_zipcode(self):
        object = super(EasyZipCodeDetailView, self).get_zipcode()
        object.save()
        return object
