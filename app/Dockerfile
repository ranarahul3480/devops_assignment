FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim

# Create a non-root user
RUN useradd -m appuser
USER appuser

WORKDIR /home/appuser/app
COPY --from=builder /root/.local /home/appuser/.local
ENV PATH=/home/appuser/.local/bin:$PATH

COPY --chown=appuser:appuser . .

EXPOSE 5000
CMD ["python", "app.py"]