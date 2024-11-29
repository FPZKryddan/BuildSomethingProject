FROM python:3.10-slim
WORKDIR /database_service
COPY . /database_service/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5002
CMD ["python", "db.py"]