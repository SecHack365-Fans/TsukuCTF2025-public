FROM node:14-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY server.js ./
COPY flag.txt ./
EXPOSE 3000
CMD ["node", "server.js"]