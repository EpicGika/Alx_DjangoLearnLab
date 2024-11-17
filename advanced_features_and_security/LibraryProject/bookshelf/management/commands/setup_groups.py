from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Article  # Replace with your actual model

class Command(BaseCommand):
    help = 'Sets up groups and permissions for the application'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Article)
        
        # Define permissions
        permissions = {
            "can_view": Permission.objects.get(codename="can_view", content_type=content_type),
            "can_create": Permission.objects.get(codename="can_create", content_type=content_type),
            "can_edit": Permission.objects.get(codename="can_edit", content_type=content_type),
            "can_delete": Permission.objects.get(codename="can_delete", content_type=content_type),
        }

        # Define groups and assign permissions
        groups_permissions = {
            "Viewers": [permissions["can_view"]],
            "Editors": [permissions["can_view"], permissions["can_create"], permissions["can_edit"]],
            "Admins": [permissions["can_view"], permissions["can_create"], permissions["can_edit"], permissions["can_delete"]],
        }

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.set(perms)
            group.save()
            self.stdout.write(self.style.SUCCESS(f'Group "{group_name}" configured successfully.'))

        self.stdout.write(self.style.SUCCESS('All groups and permissions set up successfully.'))
