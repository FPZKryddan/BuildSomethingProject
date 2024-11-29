FROM python:3.10-slim

WORKDIR /login_service
COPY . /login_service
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001
CMD ["python", "login.py"]
