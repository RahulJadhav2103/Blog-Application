# django_qrcode/adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailAddress
from django.contrib import messages


class CustomAccountAdapter(DefaultAccountAdapter):
    def respond_user_inactive(self, request, user):
        """
        Auto-resend verification email when unverified user tries to log in
        """
        email_address = EmailAddress.objects.filter(
            user=user, verified=False
        ).first()

        if email_address:
            email_address.send_confirmation(request)
        return super().respond_user_inactive(request, user)
