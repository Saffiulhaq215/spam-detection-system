# 1. Use a lightweight Python base image
FROM python:3.12-slim

# 2. Install 'uv' inside the container
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. Set the working directory
WORKDIR /app

# 4. Copy the environment files first (for faster builds)
COPY pyproject.toml uv.lock ./

# 5. Install dependencies without the project itself
RUN uv sync --frozen --no-install-project

# 6. Copy the rest of the app (src and models)
COPY src/ ./src/
COPY models/ ./models/

# 7. Expose the port FastAPI will run on
EXPOSE 8000

# 8. Start the application
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]