FROM node:20-alpine3.20
WORKDIR /workspace

COPY package.json yarn.lock server.js .
RUN yarn install

CMD ["yarn", "start"]