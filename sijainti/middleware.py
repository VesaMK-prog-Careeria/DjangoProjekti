# Middleware luokka joka estää selainta tallentamasta välimuistia

# from django.utils.deprecation import MiddlewareMixin

# class DisableCacheMiddleware(MiddlewareMixin):
#     def process_response(self, request, response):
#         response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
#         response['Pragma'] = 'no-cache'
#         response['Expires'] = '0'
#         return response

# Lisää tämä settings.py MIDDLEWARE -asetukseen:
# MIDDLEWARE = [
#     # ... muut middlewaret
#     'sijainti.middleware.DisableCacheMiddleware',
#     # ... muut middlewaret
# ]