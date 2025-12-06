# Use the slim python package
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml src/ ./ 

# Install the package system-wide
RUN pip install .

# Expose the entrypoint
ENTRYPOINT ["pyrbon"]
