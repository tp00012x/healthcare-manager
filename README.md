# Book API


## Prerequisites and Installation
[Install Docker from this link.](https://docs.docker.com/v17.12/install/#supported-platforms) 

## Setup
After having installed Docker, follow the next steps to run the app locally.

1. To build the images and services from the docker-compose.yml file run:
    ```
    docker-compose build
    ```

1. To build the images and start the containers run:
    ```
    docker-compose up
    ```
   Note: If the images do not exist it will build them.

Note: If you encounter any DB problems run:
    ```
    docker-compose down
    ```
It will stops and remove the containers, networks, volumes, and images created 
by docker-compose up.

## Getting Started
### Core app
Although, this is not necessary, I created the **core app** to support admin 
users whom will be able to use the admin interface to make changes to the wish 
list.

## Authors
* **Anthony Torres**

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) 
file for details
