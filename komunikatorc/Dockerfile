FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /komunikatorc
COPY . .
RUN uv sync
EXPOSE 8000
ENTRYPOINT uv run ./manage.py runserver