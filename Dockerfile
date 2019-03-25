# Base
FROM alpine:3.7 as base

WORKDIR /srv/app

RUN apk add --update --no-cache git gcc libc-dev python3 python3-dev jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel && pip3 wheel -r requirements.txt --wheel-dir=/srv/wheels


# Development
FROM alpine:3.7 as dev

WORKDIR /srv/app
RUN apk add --update --no-cache python3 git jpeg zlib
COPY --from=base /srv/wheels /srv/wheels
COPY requirements.txt .
RUN pip3 install --no-index --no-cache-dir --find-links=/srv/wheels -r requirements.txt

EXPOSE 8000
CMD ["./docker/run_dev.sh"]

# Testing
FROM alpine:3.7 as test

WORKDIR /srv/app
RUN apk add --update --no-cache python3 git jpeg zlib
COPY --from=base /srv/wheels /srv/wheels
COPY requirements.txt .
COPY requirements-test.txt .
RUN pip3 install --no-index --no-cache-dir --find-links=/srv/wheels -r requirements.txt
RUN pip3 install --no-cache-dir -r requirements-test.txt

CMD ["./docker/run_tests.sh"]

# Production
FROM alpine:3.7 as production

WORKDIR /srv/app
RUN apk add --update --no-cache python3 git jpeg zlib uwsgi-python3
COPY --from=base /srv/wheels /srv/wheels
COPY requirements.txt .
RUN pip3 install --no-index --no-cache-dir --find-links=/srv/wheels -r requirements.txt

EXPOSE 8000
CMD ["./docker/run_production.sh"]
