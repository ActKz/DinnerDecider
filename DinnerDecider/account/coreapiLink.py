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
}
