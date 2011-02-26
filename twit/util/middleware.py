from django.core.exceptions import ObjectDoesNotExist

class TwitterAPIMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            try:
                profile = request.user.get_profile()
            except ObjectDoesNotExist:
                request.api = None
                return
            if profile.account is not None:
                request.api = profile.api()