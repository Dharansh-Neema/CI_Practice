Here’s a **README.md** file for your project that explains how to use the application with Docker.

---

# Streamlit Power Calculator

This is a simple Streamlit application that calculates the square, cube, and fifth power of a given number. It includes a Dockerized setup to ensure easy deployment and consistent execution.

---

## Features

- Input a number and calculate its:
  - Square
  - Cube
  - Fifth power
- Lightweight and portable Dockerized setup.

---

## Prerequisites

1. **Docker**: Ensure Docker is installed on your system.
   - [Download Docker](https://www.docker.com/get-started)

---

## How to Run the Application

### Step 1: Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/Dharansh-Neema/CI_Practice.git
cd CI_Practice
```

### Step 2: Build the Docker Image

Build the Docker image for the application using the following command:

```bash
docker build -t streamlit_app .
```

### Step 3: Run the Docker Container

Run the application by starting a Docker container:

```bash
docker run -p 8051:8501 streamlit_app
```

### Step 4: Access the Application

Open your browser and go to:

```
http://localhost:8051
```

---

---

## File Structure

```
.
├── app.py           # Main Streamlit application
├── _test.py         # Unit tests
├── Dockerfile       # Docker configuration file
└── README.md        # Project documentation
```

---

## Acknowledgments

- Built using [Streamlit](https://streamlit.io/) for a simple, interactive user interface.
- Dockerized for seamless portability and deployment.

---

Feel free to contribute to this project or raise issues if you encounter any problems. Happy coding! 🚀
