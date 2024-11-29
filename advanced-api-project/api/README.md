# API Endpoints for Book Management

## List of Endpoints
- `GET /api/books/`: Retrieve a list of all books.
- `GET /api/books/<id>/`: Retrieve details of a specific book by ID.
- `POST /api/books/create/`: Create a new book (requires authentication).
- `PUT /api/books/<id>/update/`: Update a specific book (requires authentication).
- `DELETE /api/books/<id>/delete/`: Delete a specific book (requires authentication).

## Permissions
- `IsAuthenticated`: Required for create, update, and delete operations.
- `AllowAny`: Granted for read-only operations (list and detail views).
