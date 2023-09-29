FROM node:latest

WORKDIR /app

COPY ./vue/package*.json /app

RUN npm install

COPY ./vue /app

EXPOSE 5173

CMD ["npm", "run", "dev"]