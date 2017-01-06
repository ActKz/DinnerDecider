import coreapi

link = {
    "stores":{
        'List stores': coreapi.Link(
            url = '/stores/list/',
            description = 'Get list of stores',
            action = 'get',
            fields = [
                coreapi.Field(
                    name = 'keyword',
                    required = False,
                    location = 'query',
                    description = 'Searching keyword'
                    )
                ]
            ),
        'Create store': coreapi.Link(
            url = '/stores/add/',
            description = 'Add new store',
            action = 'post',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'name',
                    required = True,
                    location = 'form',
                    description = 'Store name'
                    ),
                coreapi.Field(
                    name = 'address',
                    required = True,
                    location = 'form',
                    description = 'Store address'
                    ),
                coreapi.Field(
                    name = 'phone',
                    required = True,
                    location = 'form',
                    description = 'Store phone'
                    ),
                coreapi.Field(
                    name = 'avg_price',
                    required = True,
                    location = 'form',
                    description = 'Store average price'
                    ),
                coreapi.Field(
                    name = 'tid',
                    required = True,
                    location = 'form',
                    description = 'Store type id'
                    ),
                coreapi.Field(
                    name = 'aid',
                    required = True,
                    location = 'form',
                    description = 'Store area id'
                    ),
                ]
            ),
        'Store info': coreapi.Link(
            url = '/stores/get/',
            description = 'Get single store information',
            action = 'get',
            fields = [
                coreapi.Field(
                    name = 'id',
                    required = True,
                    location = 'query',
                    description = 'Store id'
                    )
                ]
            ),
        'Update': coreapi.Link(
            url = '/stores/{store_id}/update/',
            description = 'Store information update',
            action = 'patch',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'store_id',
                    required = True,
                    location = 'path',
                    description = 'Store id'
                    ),
                coreapi.Field(
                    name = 'name',
                    required = True,
                    location = 'form',
                    description = 'Store name'
                    ),
                coreapi.Field(
                    name = 'address',
                    required = True,
                    location = 'form',
                    description = 'Store address'
                    ),
                coreapi.Field(
                    name = 'phone',
                    required = True,
                    location = 'form',
                    description = 'Store phone'
                    ),
                coreapi.Field(
                    name = 'avg_price',
                    required = True,
                    location = 'form',
                    description = 'Store average price'
                    ),
                coreapi.Field(
                    name = 'tid',
                    required = True,
                    location = 'form',
                    description = 'Store type'
                    ),
                coreapi.Field(
                    name = 'aid',
                    required = True,
                    location = 'form',
                    description = 'Store area'
                    )
                ]
            ),
        'Delete store': coreapi.Link(
            url = '/stores/{store_id}/delete/',
            description = 'Delete store from database',
            action = 'delete',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'store_id',
                    required = True,
                    location = 'path',
                    description = 'Store id'
                    )
                ]
            )
        },
    "Store type":{
        'List store types': coreapi.Link(
            url = '/storetype/',
            description = 'List all available store type',
            action = 'get',
            fields = []
            ),
        'Add store type': coreapi.Link(
            url = '/storetype/',
            description = 'Add new store type',
            action = 'post',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'name',
                    required = True,
                    location = 'form',
                    description = 'Type name'
                    )
                ]
            ),
        'Delete store type': coreapi.Link(
            url = '/storetype/{type_id}/',
            description = 'Delete store type',
            action = 'delete',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'type_id',
                    required = True,
                    location = 'path',
                    description = 'Type id'
                    )
                ]
            ),
    },
    "Area":{
        'List area': coreapi.Link(
            url = '/area/',
            description = 'List area',
            action = 'get',
            fields = []
            ),
        'Add area': coreapi.Link(
            url = '/area/',
            description = 'Add new area',
            action = 'post',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'name',
                    required = True,
                    location = 'form',
                    description = 'Area name'
                    ),
                ]
            ),
        'Delete area': coreapi.Link(
            url = '/area/{area_id}/',
            description = 'Delete area from database',
            action = 'delete',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'area_id',
                    required = True,
                    location = 'path',
                    description = 'area id'
                    )
                ]
            ),
    },
    "Search":{
        "Fuzzy search": coreapi.Link(
            url = '/search/store/',
            description = 'Store name fuzzy search',
            action = 'get',
            fields = [
                coreapi.Field(
                    name = 'keyword',
                    required = False,
                    location = 'query',
                    description = 'Searching keyword'
                    )
                ]
        ),
        "Type search": coreapi.Link(
            url = '/search/type/',
            description = 'List the matched stores',
            action = 'get',
            fields = [
                coreapi.Field(
                    name = 'tid',
                    required = True,
                    location = 'query',
                    description = 'Type id'
                    )
                ]
        ),
        "Area search": coreapi.Link(
            url = '/search/area/',
            description = 'List the matched stores',
            action = 'get',
            fields = [
                coreapi.Field(
                    name = 'aid',
                    required = True,
                    location = 'query',
                    description = 'Area id'
                    )
                ]
        ),
        "Type & area search": coreapi.Link(
            url = '/search/type-area-search/',
            description = 'List the matched stores',
            action = 'get',
            fields = [
                coreapi.Field(
                    name = 'aid',
                    required = True,
                    location = 'query',
                    description = 'Area id',
                    ),
                coreapi.Field(
                    name = 'tid',
                    required = True,
                    location = 'query',
                    description = 'Type id'
                    )
                ]
        ),
        "Price search": coreapi.Link(
            url = '/search/price-limit/',
            description = 'List the matched stores',
            action = 'get',
            fields = [
                coreapi.Field(
                    name = 'llim',
                    required = True,
                    location = 'query',
                    description = 'Price lower limit'
                    ),
                coreapi.Field(
                    name = 'ulim',
                    required = True,
                    location = 'query',
                    description = 'Price upper limit'
                    ),
                ]
        ),
    },
}
