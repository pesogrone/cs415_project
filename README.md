# E-commerce Website with AWS EC2 and S3(in progress)

Welcome to the documentation for our e-commerce website project for the class 415 Operating Systems. This project involves creating a website for renting products using virtual machines (AWS EC2) as the backend and AWS S3 for storage.

## Getting Started

To get started with our project, follow these steps:

1. Clone this repository to your local machine.
2. Install any necessary dependencies.
3. Set up your AWS account and configure AWS services (EC2 and S3).
4. Deploy your backend on AWS EC2 instances.
5. Configure your frontend to communicate with the backend APIs.
6. Use AWS S3 to store product images and other static assets.

## Backend

### AWS EC2

We use AWS EC2 instances to host our backend APIs. Each EC2 instance serves as a virtual server running our backend application, handling requests from the frontend, and interacting with the database.

### Endpoints

- **GET /api/products**: Retrieves a list of available products for renting.
- **GET /api/products/{productId}**: Retrieves details of a specific product identified by its ID.
- **POST /api/orders**: Places a new order for renting a product.
- **GET /api/orders**: Retrieves a list of all orders placed by customers.
- **GET /api/orders/{orderId}**: Retrieves details of a specific order identified by its ID.

### Authentication

Authentication mechanisms can be implemented using AWS Identity and Access Management (IAM) or JSON Web Tokens (JWT), depending on the requirements of the project.

## Frontend

The frontend of our e-commerce website is responsible for providing a user-friendly interface for customers to browse products, place orders, and manage their accounts. It communicates with the backend APIs to fetch data and perform actions.(in progress)

## Storage

### AWS S3

We use AWS S3 (Simple Storage Service) to store product images and other static assets used by the frontend. S3 provides scalable and secure storage for our website's assets, ensuring high availability and durability.(in progress)


## Contributing

We welcome contributions from the community to improve our e-commerce website project. If you'd like to contribute, please fork this repository, make your changes, and submit a pull request. We appreciate your contributions!

