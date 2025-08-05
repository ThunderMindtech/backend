# backend

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.13+** - Required for this project
- **uv** - Fast Python package installer and resolver

### Installing uv

If you don't have uv installed, you can install it using one of the following methods:

**On macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Using pip:**

```bash
pip install uv
```

**Using Homebrew (macOS):**

```bash
brew install uv
```

## Setup

1. **Clone or navigate to the project directory:**

   ```bash
   cd backend
   ```

2. **Install dependencies using uv:**

   ```bash
   uv sync
   ```

   This will create a virtual environment and install all dependencies specified in `pyproject.toml`.

3. **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate
   ```

   Or if you prefer to run commands without activating:

   ```bash
   uv run manage.py runserver
   ```

## Usage

Run the main application:

```bash
# If virtual environment is activated
python manage.py runserver

# Or using uv directly
uv run manage.py runserver
```

## Development

### Adding new dependencies

To add a new dependency:

```bash
uv add package-name
```

### Running in development mode

```bash
uv run manage.py runserver
```

### Project Structure

```
backend/
├── manage.py           # Main application entry point
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock             # Locked dependency versions
└── README.md           # This file
└── backend             # Django Configuration
```

## Troubleshooting

- Ensure Python 3.13+ is installed and available in your PATH
- If you encounter issues with uv, try updating it: `uv self update`

## License

This project is part of the TMT (ThunderMindtech) organization.
