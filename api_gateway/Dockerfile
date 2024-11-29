FROM python:3.10-slim

WORKDIR /api_gateway
COPY . /api_gateway
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "gateway.py"]