ARG pythonversion=3.12-slim
FROM python:${pythonversion}
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
 