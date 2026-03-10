# QR Code Generator

A command-line Python application that generates QR code images from URLs. Dockerized for easy deployment and portability.

## Features

- Generate QR codes from any valid URL
- Customizable fill and background colors via environment variables
- Timestamped output filenames
- URL validation
- Runs as a non-root user inside Docker for security

## Prerequisites

- Python 3.12+ (for local usage)
- Docker (for containerized usage)

## Local Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Run with the default URL:

```bash
python main.py
```

Run with a custom URL:

```bash
python main.py --url https://www.example.com
```

Generated QR codes are saved to the `qr_codes/` directory.

## Environment Variables

| Variable       | Description                  | Default     |
|----------------|------------------------------|-------------|
| `QR_CODE_DIR`  | Output directory for QR codes | `qr_codes` |
| `FILL_COLOR`   | QR code fill color           | `red`       |
| `BACK_COLOR`   | QR code background color     | `white`     |

## Docker

Build the image:

```bash
docker build -t qr-code-generator-app .
```

Run the container:

```bash
docker run --name qr-generator qr-code-generator-app
```

Run with a custom URL and a volume mount to retrieve the output:

```bash
docker run --name qr-generator -v ./qr_codes:/app/qr_codes qr-code-generator-app --url https://www.njit.edu
```

## Running Tests

```bash
pytest tests/ -v
```

## CI/CD

A GitHub Actions workflow (`.github/workflows/docker-build.yml`) runs on every push and pull request to `main`. It:

1. Installs dependencies and runs the test suite
2. Builds the Docker image
3. Runs the container and verifies a QR code is generated
