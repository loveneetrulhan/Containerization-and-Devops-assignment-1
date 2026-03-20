FROM postgres:13

ENV POSTGRES_DB=mydb
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=pass

COPY init.sql /docker-entrypoint-initdb.d/
