"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),

    # Blog Routes
    Get('/blog', 'BlogController@show')
]

from masonite.auth import Auth 
ROUTES += Auth.routes()
# masonite-inertia demo routes
ROUTES += [
    Get("/inertia", "InertiaDemoController@show"),
    Get("/inertia-hello", "InertiaDemoController@hello"),
]
