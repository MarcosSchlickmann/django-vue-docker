# estágio de compilação
FROM node:lts-alpine as build-stage

WORKDIR /front
COPY app/package*.json /front/
RUN npm install -g @vue/cli
RUN npm install
COPY app/ /front/

RUN npm run build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /front/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]