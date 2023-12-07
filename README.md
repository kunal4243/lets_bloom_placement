# Creating API for handling book data
I have created these APIs for the placement test for Letsbloom.

## Working with the code.

First, host the `library_api.py` file locally or in a cloud to get a link to the host. In my case, it was locally hosted with the link:  `http://127.0.0.1:5000`

The database is hosted online and is free but with a limit of 5 MB. So before filling it out, please clear the old database by calling the delete endpoint mentioned below. The database could be changed too, by changing the link in the code itself.

For each of the endpoint implementations, see the details below.



## Endpoint 0: Delete all books.

**Endpoint: DELETE /api/books**

This endpoint deletes all the books to clear memory.

## Endpoint 1: Retrieve All Books

**Endpoint: GET /api/books**

This endpoint makes an HTTP GET request to retrieve a list of books. The request does not require any parameters or payload. 

**Response**

The response will have a status code of 200, indicating a successful request. The body of the response will contain an array of books, where each book object includes the author, id, and title.

**Example response body:**
```
{
    "books": [
        {
            "author": "",
            "id": 0,
            "title": ""
        }
    ]
}
```




## Endpoint 2: Add a New Book

**Endpoint: POST /api/books**

This endpoint allows you to add a new book to the database.

### Request Body:

**title** (string, required): The title of the book.

**author** (string, required): The author of the book.

JSON Format Example
Body type- application/json

```
{
    "title": "hello",   
    "author": "kunal"
}
```

Response

Status: 400

error (string): An error message indicating the reason for the request failure.

Status: Book added

Response:
```
{
    "message": "Book added successfully."
}
```

Status: 400 Bad Request

error(message): Book already exists.

## Endpoint 3: Update Book Details
**Endpoint: PUT /api/books/{id}**

id(int, required): id the id of the row we want to modify.

This endpoint allows updating a specific book by sending an HTTP PUT request to the specified URL. The request should include the book title and author in the raw request body.

**Request Body**

**title** (string, required): The title of the book.

**author** (string, required): The author of the book.


Response

Status: 200 OK

message (string): A message confirming the successful update.

Status: 404

message (string): Book not found or not in the list


Example Request:
\api\book\2 (PUT)
```
{
    "title": "hello world"
}
```
Updates the row number 2 if it exists by changing title to "hello world"









## Credits
[Rest API with flask and sqlalchemy- Traversy Media](https://www.youtube.com/watch?v=PTZiDnuC86g)

[MySQL Host](https://www.freemysqlhosting.net/)

[Tested using the postman](https://www.postman.com/api-documentation-tool/)


