# estágio de compilação
FROM node:lts-alpine as build-stage

WORKDIR /front
COPY app/package*.json /front/
RUN npm install -g @vue/cli
RUN npm install
COPY app/ /front/

CMD npm run serve
