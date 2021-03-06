from __future__ import unicode_literals
from django.db.models import get_model
from django.http import HttpResponse
from django.utils import simplejson
from .compat import cmp_to_key, compare_func


def filterchain(request, app, model, field, value, manager=None):
    model_class = get_model(app, model)
    if value == '0':
        keywords = {str("%s__isnull" % field): True}
    else:
        keywords = {str(field): str(value)}
    if manager is not None and hasattr(model_class, manager):
        queryset = getattr(model_class, manager)
    else:
        queryset = model_class._default_manager
    results = list(queryset.filter(**keywords))
    results.sort(key=cmp_to_key(compare_func))
    result = []
    for item in results:
        result.append({'value': item.pk, 'display': str(item)})
    json = simplejson.dumps(result)
    return HttpResponse(json, mimetype='application/json')


def filterchain_all(request, app, model, field, value):
    model_class = get_model(app, model)
    if value == '0':
        keywords = {str("%s__isnull" % field): True}
    else:
        keywords = {str(field): str(value)}
    results = list(model_class._default_manager.filter(**keywords))
    results.sort(key=cmp_to_key(compare_func))
    final = []
    for item in results:
        final.append({'value': item.pk, 'display': str(item)})
    results = list(model_class._default_manager.exclude(**keywords))
    results.sort(key=cmp_to_key(compare_func))
    final.append({'value': "", 'display': "---------"})

    for item in results:
        final.append({'value': item.pk, 'display': str(item)})
    json = simplejson.dumps(final)
    return HttpResponse(json, mimetype='application/json')
