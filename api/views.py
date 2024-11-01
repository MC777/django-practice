from django.http import JsonResponse

def getRoutes(request):
    routes = [
        {'GET':'api/projects'},
        {'GET':'api/projects/id'},
        {'GET':'api/projects/id/vote'},

        {'GET':'api/users/token'},
        {'GET':'api/users/token/refresh'},
    ]
    return JsonResponse(routes)