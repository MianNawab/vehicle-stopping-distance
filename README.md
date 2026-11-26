# Vehicle Stopping Distance Simulator

A Python-based vehicle stopping distance simulator that calculates reaction distance, braking distance and total stopping distance under different road conditions and vehicle speeds.

## Overview

This project explores the relationship between vehicle speed, driver reaction time, road friction and road gradient in determining stopping distance.

It also serves as a practical project for learning software engineering practices, including automated testing, version control, CI/CD and Docker containerization.

## Features

- Convert vehicle speed from km/h to m/s.
- Calculate reaction distance.
- Calculate braking distance.
- Account for different road conditions: dry, wet, snow and icy.
- Consider road gradient.
- Compare stopping distances at multiple vehicle speeds.
- Visualize stopping-distance results.

## Technologies Used

- Python 3.12
- Matplotlib
- pytest
- pytest-cov
- Ruff
- Git and GitHub
- GitHub Actions
- Docker
- GitHub Container Registry (GHCR)

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/MianNawab/vehicle-stopping-distance.git
cd vehicle-stopping-distance
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements-dev.txt
```

## Run the Application

```bash
python main.py
```

Follow the prompts to enter reaction time, road gradient, road conditions and vehicle speeds.

## Run Tests

```bash
python -m pytest --cov=main --cov-report=term-missing
```

## Docker

Build the Docker image:

```bash
docker build -t vehicle-stopping-distance .
```

Run the container interactively:

```bash
docker run -it vehicle-stopping-distance
```

## CI/CD Pipeline

GitHub Actions automates:

- Ruff linting and formatting checks.
- Automated testing using pytest.
- Test coverage reporting.
- Docker image building.
- Docker image publishing to GitHub Container Registry after changes are pushed to the main branch.

## Docker Image

The published image is available through GitHub Container Registry:

```bash
docker pull ghcr.io/miannawab/vehicle-stopping-distance:latest
```

Run it:

```bash
docker run -it ghcr.io/miannawab/vehicle-stopping-distance:latest
```

## Future Improvements

- Expand automated test coverage.
- Improve input validation and error handling.
- Explore additional vehicle dynamics parameters.
- Extend the simulator with more advanced visualization.

---

**Project developed as part of my practical learning journey in Python software development and automotive engineering.**