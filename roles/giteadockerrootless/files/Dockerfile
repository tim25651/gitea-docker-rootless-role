FROM alpine

RUN apk add --no-cache inotify-tools

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME ["/source", "/destination"]

ENTRYPOINT ["/entrypoint.sh"]
