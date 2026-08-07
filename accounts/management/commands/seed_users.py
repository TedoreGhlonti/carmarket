import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "შექმნის საწყის superuser-ს, თუ ის ჯერ არ არსებობს"

    def handle(self, *args, **options):
        admin_password = os.environ.get("DJANGO_ADMIN_PASSWORD", "changeme123")

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@carmarket.com",
                password=admin_password,
            )
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' შეიქმნა"))
        else:
            self.stdout.write("Superuser 'admin' უკვე არსებობს, გამოტოვება")