from django.http import HttpResponse


def test(request):
    data = "this is a test"

    print(data)
    return HttpResponse(data, content_type='application/json')
