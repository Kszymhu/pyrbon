FROM python:3.13
WORKDIR /usr/local/pyrbon

COPY . .
RUN pip install .

RUN useradd pyrbon
USER pyrbon

ENTRYPOINT ["pyrbon"]
