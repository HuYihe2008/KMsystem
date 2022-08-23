FROM huyihe/kmsystem:dev
LABEL 维护者="2812856215@qq.com"

# 备选数据库Sqlite \Mysql \ PostgreSQL
ENV DB_TYPE='Sqlite'

RUN sed -i "s|'postgresql+psycopg2://\${DB_USER}:\${DB_PASSWORD}@\${DB_HOST}:\${DB_PORT}/\${DB_DATABASE}'|'\`echo \$DATABASE_URL \| sed \'s/postgres/postgresql\\\+psycopg2/\'\`'|g" docker-entrypoint.sh && \
    sed -i '$d' docker-entrypoint.sh && \
    echo "gunicorn -k gevent --bind 0.0.0.0:\${PORT} --workers 4 app:app" >> docker-entrypoint.sh

EXPOSE $PORT

ENTRYPOINT [ "/usr/src/app/docker-entrypoint.sh" ]
