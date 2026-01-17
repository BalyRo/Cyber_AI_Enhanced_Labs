FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app


COPY pyproject.toml uv.lock ./


RUN uv pip install --system .

COPY . .


ENV PATH="/usr/local/bin:$PATH"


CMD ["devui", "app", "--host", "0.0.0.0", "--port", "8080"]
