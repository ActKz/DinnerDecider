import coreapi
link = {
    "User":{
        'User info': coreapi.Link(
            url = '/users/user-info/',
            description = "Show authed user information",
            action = 'get',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                ]
            ),
        'Create User': coreapi.Link(
            url = '/users/create-account/',
            description = "Create account",
            action = 'post',
            fields = [
                coreapi.Field(
                    name = 'username',
                    required = True,
                    location = 'form',
                    description = 'Account name'
                    ),
                coreapi.Field(
                    name = 'email',
                    required = True,
                    location = 'form',
                    description = 'Account email'
                    ),
                coreapi.Field(
                    name = 'password',
                    required = True,
                    location = 'form',
                    description = 'Account password'
                    ),
                ]
            ),
        'Change password': coreapi.Link(
            url = '/users/change-password/',
            description = 'Change account password',
            action = 'post',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'password',
                    required = True,
                    location = 'form',
                    description = 'Account password'
                    )
                ]
            ),
        'Change email': coreapi.Link(
            url = '/users/change-email/',
            description = 'Change account email',
            action = 'post',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'email',
                    required = True,
                    location = 'form',
                    description = 'Account email'
                    )
                ]
            ),
        'Delete account': coreapi.Link(
            url = '/users/delete-account/',
            description = 'Delete authed user',
            action = 'get',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                ]
            ),
    },
    "JWT":{
        'JWT auth': coreapi.Link(
            url = '/api-token-auth/',
            description = 'JWT auth login',
            action = 'post',
            fields = [
                coreapi.Field(
                    name = 'username',
                    required = True,
                    location = 'form',
                    description = 'Account name'
                    ),
                coreapi.Field(
                    name = 'password',
                    required = True,
                    location = 'form',
                    description = 'Account password'
                    )
                ]
            ),
        'JWT token refresh': coreapi.Link(
            url = '/api-token-refresh/',
            description = 'Refresh token',
            action = 'post',
            fields = [
                coreapi.Field(
                    name = 'token',
                    required = True,
                    location = 'form',
                    description = 'Authed token'
                    )
                ]
            ),
        'Logout': coreapi.Link(
            url = '/api-token-logout/',
            description = 'Logout user',
            action = 'get',
            fields = []
            ),
    },
    "User Favorite list":{
        "Add": coreapi.Link(
            url = '/favlist/add/',
            description = "Add favorite list",
            action = 'post',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'sid',
                    required = True,
                    location = 'form',
                    description = 'store id',
                    type = 'array'
                    ),
                coreapi.Field(
                    name = 'listname_id',
                    required = True,
                    location = 'form',
                    description = 'Favorite list name'
                    ),
                ]
            ),
        "List": coreapi.Link(
            url = '/favlist/get/',
            description = 'List favorite list',
            action = 'get',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                ]
            ),
        "Delete": coreapi.Link(
            url = '/favlist/{favlist_id}/delete/',
            description = 'Delete favorite list element',
            action = 'delete',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'favlist_id',
                    required = True,
                    location = 'path',
                    description = 'List element id'
                    ),
                ]
            ),
        "Update": coreapi.Link(
            url = '/favlist/{favlist_id}/update/',
            description = 'Change the elements\' listname',
            action = 'patch',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'favlist_id',
                    required = True,
                    location = 'path',
                    description = 'List element id'
                    ),
                coreapi.Field(
                    name = 'listname_id',
                    required = True,
                    location = 'form',
                    description = 'List name id'
                    ),
                coreapi.Field(
                    name = 'sid',
                    required = True,
                    location = 'form',
                    description = 'store id'
                    ),
                ]
            ),
        },
    "User Favorite List Name":{
        "List": coreapi.Link(
            url = '/favlistname/get/',
            description = 'List all listname',
            action = 'get',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                ]
            ),
        "Add": coreapi.Link(
            url = '/favlistname/add/',
            description = 'Add new favorite list',
            action = 'post',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'listname',
                    required = True,
                    location = 'form',
                    description = 'List name'
                    ),
                ]
            ),
        "Update": coreapi.Link(
            url = '/favlistname/{listname_id}/update/',
            description = 'Change list name',
            action = 'patch',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'listname_id',
                    required = True,
                    location = 'path',
                    description = 'Listname id'
                    ),
                coreapi.Field(
                    name = 'listname',
                    required = True,
                    location = 'form',
                    description = 'List name'
                    ),
                ]
            ),
        "Delete": coreapi.Link(
            url = '/favlistname/{listname_id}/delete/',
            description = 'Delete list',
            action = 'delete',
            fields = [
                coreapi.Field(
                    name = 'Authorization',
                    required = False,
                    location = 'header',
                    description = 'JWT token'
                    ),
                coreapi.Field(
                    name = 'listname_id',
                    required = True,
                    location = 'path',
                    description = 'Listname id'
                    ),
                ]
            ),
        },
}
