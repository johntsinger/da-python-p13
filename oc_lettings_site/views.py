from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Index view.

    Params:
        - request (HttpRequest) : Django request object.

    Returns:
        - render (func) : Combines a given template with a given
        context dictionary and returns an HttpResponse object with
        that rendered text.
    """
    return render(request, 'index.html')


def custom_404(request, template_name='404.html', *args, **kwargs):
    """
    Error 404 view.

    Params:
        - request (HttpRequest) : Django request object.
        - template_name (str) : the template name.
            default = '404.html'

    Returns:
        - render (func) : Combines a given template with a given
        context dictionary and returns an HttpResponse object with
        that rendered text.
    """
    return render(request, template_name, status=404)


def custom_500(request, template_name='500.html', *args, **kwargs):
    """
    Error 500 view.

    Params:
        - request (HttpRequest) : Django request object.
        - template_name (str) : the template name.
            default = '500.html'

    Returns:
        - render (func) : Combines a given template with a given
        context dictionary and returns an HttpResponse object with
        that rendered text.
    """
    return render(request, template_name, status=500)
