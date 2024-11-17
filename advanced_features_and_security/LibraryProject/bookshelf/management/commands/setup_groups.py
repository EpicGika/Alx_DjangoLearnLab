from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_groups():
    # Create the groups
    editors_group, created = Group.objects.get_or_create(name='Editors')
    viewers_group, created = Group.objects.get_or_create(name='Viewers')
    admins_group, created = Group.objects.get_or_create(name='Admins')

    # Get content type for the Book model
    book_content_type = ContentType.objects.get_for_model(Book)

    # Get permissions for Book model
    can_view_permission = Permission.objects.get(codename='can_view', content_type=book_content_type)
    can_create_permission = Permission.objects.get(codename='can_create', content_type=book_content_type)
    can_edit_permission = Permission.objects.get(codename='can_edit', content_type=book_content_type)
    can_delete_permission = Permission.objects.get(codename='can_delete', content_type=book_content_type)

    # Assign permissions to groups
    editors_group.permissions.set([can_create_permission, can_edit_permission])
    viewers_group.permissions.set([can_view_permission])
    admins_group.permissions.set([can_view_permission, can_create_permission, can_edit_permission, can_delete_permission])

    # Save the groups
    editors_group.save()
    viewers_group.save()
    admins_group.save()
