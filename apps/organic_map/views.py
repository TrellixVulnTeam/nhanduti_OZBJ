from django.views import generic
from watson import search as watson
from apps.organic_fair.models import OrganicFair
from apps.organic_farmer.models import OrganicFarmer

from djgeojson.views import GeoJSONLayerView


class OrganicMap(generic.ListView):

    model = OrganicFarmer
    template_name = 'organic_map/organic_map.html'
    context_object_name = 'organic_map_itens'

    def get_queryset(self):
        queryset = OrganicFarmer.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)

        return queryset


class OrganicMapJson(GeoJSONLayerView, generic.ListView):

    model = OrganicFarmer
    template_name = 'organic_map/organic_map.html'
    context_object_name = 'organic_map_itens'

    '''def get_queryset(self):
        queryset = OrganicFarmer.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)

        return queryset'''

    def get(self):
        queryset = OrganicFarmer.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)

        return queryset