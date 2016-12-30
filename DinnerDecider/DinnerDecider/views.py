import coreapi
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from account import coreapiLink as accAPI
from store import coreapiLink as stoAPI

content = {}
content.update(accAPI.link)
content.update(stoAPI.link)

document = coreapi.Document(
                title='DinnerDecider API',
                url='http://140.113.27.54:8001',
                content=content
)

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    return response.Response(document)
