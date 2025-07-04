FROM python:3.10-slim

# Setting working directory
WORKDIR /app

# Copy app and install, our base code folder is src
COPY ./src/  .

RUN pip install --no-cache-dir -r requirements.txt

# Expose the default FastAPI port
EXPOSE 8000

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]