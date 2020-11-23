"""Web Routes."""

from masonite.auth import Auth
from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),
    Get('auth/github', 'SocialAuthController@login').name('auth.github.login'),
    Get('auth/github/callback',
        'SocialAuthController@callback').name('auth.github.callback'),

    # Blog Routes
    Get('/blog', 'BlogController@show')
]

ROUTES += Auth.routes()
