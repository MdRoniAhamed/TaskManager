from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives 


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # Get Reset Password Password Url
    reset_password_url = "http://127.0.0.1:8000/user/reset_password/{}".format(reset_password_token.key)
    token = reset_password_token.key

    # Send email Data
    content = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': reset_password_url,
        'token': token
    }

    # render email text
    email_html_message = render_to_string('email/password_reset_email.html',content)
    email_text_message = render_to_string('email/password_reset_email.txt', content)

    # Send Email

    msg = EmailMultiAlternatives(
        "Password Reset{title}".format(title=reset_password_token.user.username),
        email_text_message,
        "noreply@yourdomain.com",
        [reset_password_token.user.email]
    )

    msg.attach_alternative(email_html_message,'text/html')
    msg.send()
