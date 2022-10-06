from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        email='huzaifa.officialmail@gmail.com'
        send_otp_to_email(email)

        self.stdout.write(self.style.SUCCESS(
            'Sent!'
        ))