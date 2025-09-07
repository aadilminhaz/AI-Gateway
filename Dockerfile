FROM python:3.11

# Setting working directory
WORKDIR /app

# Copy app and install, our base code folder is src
COPY main.py .
COPY .env .
COPY ./src/  ./src/
COPY requirements.txt .

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Expose the default FastAPI port
EXPOSE 8000

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]