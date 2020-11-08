"""A SocialAuthController Module."""

from masonite.view import View
from socialite import Socialite
from masonite.request import Request
from masonite.controllers import Controller


class SocialAuthController(Controller):
    """SocialAuthController Controller Class."""

    def login(self, socialite: Socialite):
        return socialite.driver('github').redirect()

    def callback(self, view: View, request: Request, socialite: Socialite):
        user = socialite.driver('github').user()
        fullname = user.fullname

        return view.render('welcome', {'fullname': fullname})
