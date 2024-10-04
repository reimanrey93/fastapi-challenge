# FastAPI Challenge

Welcome to the **fastapi-challenge** project, where you can interact with the Star Wars universe! This guide will help you get started, providing instructions on how to set up the project using Docker, populate the database, and access the API documentation. Enjoy the power of the Force while coding!

## Technologies Used

- **Python 3.9**: The programming language of the project.
- **FastAPI**: A modern, fast web framework for building APIs with Python 3.6+.
- **SQLite**: A lightweight and serverless database engine.
- **SQLAlchemy**: ORM for working with the database.
- **Docker**: For containerizing the application.
- **pytest**: For unit testing the project.
- **Pydantic**: Data validation and settings management using Python type annotations.

## Prerequisites

To run the project, you need the following installed:

- **Docker**: To build and run the containerized application.
- **Postman or REST Client**: To test the API endpoints and import/export collections (optional).

## Project Setup

### Folder Structure

The project is organized as follows:

- **app/**: The core application directory.
  - **api/**: Contains the main API endpoints.
    - **v1/**: The versioned folder for API endpoints.
      - **endpoints/**: Directory containing the `characters.py` file that handles the Star Wars character routes.
  - **core/**: Core configurations and utilities (if any).
  - **domain/**: Contains the models and schemas for database objects.
    - **models.py**: The database model definitions.
    - **schemas.py**: Pydantic schemas for data validation.
  - **infrastructure/**: Contains database-related files.
    - **db/**: The directory for database configurations.
      - **database.py**: Establishes the connection to the SQLite database.
      - **init_db.py**: Handles database initialization.
  - **tests/**: Unit tests for the project, written with `pytest`.
  - **utils/**: Utility scripts for the project.
    - **load_characters.py**: Script to populate the database with Star Wars characters.
    - **media/**: Directory containing images and other media files for the API documentation.

### Setting up the Project

1. **Clone the repository**
   ```
   git clone https://github.com/reimanrey93/fastapi-challenge.git
   cd fastapi-challenge
   ```

2. **Build and Run Docker Container**
   ```
   docker compose build
   docker compose up
   ```

   The application will be available on `http://localhost:8000`.

3. **Access API Documentation**
   Navigate to `http://localhost:8000/docs` to access the automatically generated Swagger UI.

4. **Populate the Database**

   Inside the Docker container, execute the following to populate the database:
   ```
   docker exec -it <container_id> python /app/app/utils/load_characters.py
   ```
   Replace `<container_id>` with the ID of your running container.

5. **Run Unit Tests**
   To run unit tests with `pytest`, use the following command:
   ```
   docker exec -it <container_id> pytest /app/app/tests
   ```

---

### Accessing API Endpoints

After setting up the project, the following endpoints are available:

- **GET /api/v1/character/getAll**: Retrieve all characters.
- **GET /api/v1/character/get/{id}**: Retrieve a character by ID.
- **POST /api/v1/character/add**: Add a new character to the database.
- **DELETE /api/v1/character/delete/{id}**: Delete a character by ID.

```
                    ____
                 _.' :  `._
             .-.'`.  ;   .'`.-.
    __      / : ___\ ;  /___ ; \      __
  ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
       `:-.._J '-.-'L__ `-- ' L_..-;'
         "-.__ ;  .-"  "-.  : __.-"
             L ' /.------.\ ' J
              "-.   "--"   .-"
             __.l"-:_JL_;-";.__
          .-j/'.;  ;""""  / .'\"-.
        .' /:`. "-.:     .-" .';  `.
     .-"  / ;  "-. "-..-" .-"  :    "-.
  .+"-.  : :      "-.__.-"      ;-._   \
  ; \  `.; ;                    : : "+. ;
  :  ;   ; ;                    : ;  : \:
 : `. "-" ;                     :  "-'  :
  ;    -'                       :      ;


May the Force be with you! 🚀
