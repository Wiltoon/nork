# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.6

ENV PYTHONUNBUFFERED 1

WORKDIR /nork
# Install pip requirements
COPY requeriments.txt .
RUN pip install -r requeriments.txt

# PORT
EXPOSE 8080

COPY . .
# ENVS
ENV FLASK_APP='main.py'
ENV HOST_URL='postgresql+psycopg2://postgres:postgres@localhost:5434/nork'
ENV VEHICLE_LIMIT=3

#ENV PATH="/py/bin:$PATH"

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]