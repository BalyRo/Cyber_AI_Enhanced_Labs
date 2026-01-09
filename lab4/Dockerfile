FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# העתקת הגדרות
COPY pyproject.toml uv.lock ./

# התקנה ישירה למערכת
RUN uv pip install --system .

# העתקת כל שאר הקבצים
COPY . .

# הגדרת נתיב (ליתר ביטחון)
ENV PATH="/usr/local/bin:$PATH"

# הרצת הפקודה הישירה שהחבילה יוצרת
CMD ["devui", "app", "--host", "0.0.0.0", "--port", "8080"]