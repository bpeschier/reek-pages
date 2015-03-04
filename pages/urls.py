from .urlresolvers import PageResolver


#
# Dynamic page confs
#

class URLConfWrapper:
    """
    Mimics a urls.py urlconf interface so RegexURLResolver can work with it
    """

    def __init__(self, resolver):
        self.resolver = resolver

    @property
    def urlpatterns(self):
        return [self.resolver, ]


def include_pages(page_model, app_name=None, namespace=None):
    """
    Include page urls within a url pattern.

    Usage:

    urlpatterns = [
        url(r'^subpath/', include_pages(Page)),
    ]
    """
    return URLConfWrapper(PageResolver(page_model, app_name, namespace)), app_name, namespace
