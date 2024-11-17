# Permissions and Groups Setup

## Custom Permissions
- Added to `Article` model: `can_view`, `can_create`, `can_edit`, `can_delete`.

## Groups
- **Viewers**: Can view articles.
- **Editors**: Can view, create, and edit articles.
- **Admins**: Full access.

## Usage in Views
- Decorators like `@permission_required` enforce permissions.
- Example: 
  - View articles: `@permission_required('app_name.can_view', raise_exception=True)`

## Testing
1. Assign users to groups.
2. Log in and test access to views.
