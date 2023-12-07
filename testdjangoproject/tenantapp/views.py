import json

from django.http.request import HttpRequest
from django.http.response import HttpResponse

from tenantapp.models import House


def houses(request: HttpRequest) -> HttpResponse:
    # TODO: add nested table using FK
    # TODO: debug .prefetch_related('choice_set')
    return HttpResponse(
        json.dumps({
            'tenant': request.tenant.name,
            'houses': [
                {
                    'id': house.id,
                    'addr': house.addr,
                    'desc': house.desc,
                    "created_at": house.created_at,
                    "updated_at": house.updated_at,

                } for house in House.objects.all()
            ],
        }),
        content_type='application/json',
    )
