FROM node:13.12.0-alpine

WORKDIR /usr/src/app

ENV PATH /app/node_modules/.bin:$PATH
COPY package.json ./
COPY package-lock.json ./

COPY package.json ./
COPY package-lock.json ./
COPY yarn.lock .

RUN yarn install

COPY public/ ./public/
COPY src/ ./src/

EXPOSE 3000

CMD yarn run start
