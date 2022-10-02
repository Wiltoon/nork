# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.6

WORKDIR /nork

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# PORT
EXPOSE 5000

COPY . .

# ENVS
ENV HOST_URL="sqlite:///server.db"
ENV VEHICLE_LIMIT=3

CMD ["flask", "--app", "main.py", "run", "--host", "0.0.0.0", "-p", "5000"]