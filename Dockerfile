FROM python:3.12-slim as build
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR app/

# Download depend1encies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/uv to speed up subsequent builds.
# Leverage a bind mount to uv.lock to avoid having to copy them into this layer.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    /bin/uv sync --no-dev --no-install-project --frozen

RUN ls -al && sleep 11

FROM python:3.12-slim

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=build /app/.venv /app/.venv
ENV VIRTUAL_ENV=/app/.venv/
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser


# Switch to the non-privileged user to run the application.
USER appuser

# Copy the source code into the container.
COPY ./komunikatorc .

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD ["python", "./manage.py", "runserver"]