FROM python:3.11

ARG ENV DEBIAN_FRONTEND noninteractive
    
    # install Microsoft SQL Server requirements.
ENV ACCEPT_EULA=Y
RUN apt-get update -y && apt-get update \
    && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev
    
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
      && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
      && apt-get update \
      && apt-get install -y --no-install-recommends --allow-unauthenticated msodbcsql17 mssql-tools \
      && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
      && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
    
RUN apt-get -y clean

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port FastAPI is running on
EXPOSE 8081

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
