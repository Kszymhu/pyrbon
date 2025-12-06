FROM python:3.11
WORKDIR /usr/local/pyrbon

COPY pyproject.toml src/ ./ 
RUN pip install .

RUN useradd pyrbon
USER pyrbon

ENTRYPOINT ["pyrbon"]
