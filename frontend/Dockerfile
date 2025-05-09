# Use official Node.js image for React
FROM node:20-alpine
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
RUN npm install --legacy-peer-deps
COPY ./src ./src
COPY ./public ./public
EXPOSE 3000
CMD ["npm", "start"]
