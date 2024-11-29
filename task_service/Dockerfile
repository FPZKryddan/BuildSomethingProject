FROM python:3.10-slim

WORKDIR /task_service
COPY . /task_service
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5003
CMD ["python", "task.py"]
