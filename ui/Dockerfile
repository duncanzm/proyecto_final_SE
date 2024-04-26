# Build step
FROM node:20.11.1-alpine3.19 as angular-build-step
WORKDIR /app
COPY . .
RUN npm i @angular/cli@17 -g
WORKDIR /app/
RUN npm install
RUN ng build

# # Run step
FROM nginx:1.25
RUN rm /usr/share/nginx/html/index.html
COPY --from=angular-build-step /app/dist/ui/browser/ /usr/share/nginx/html
EXPOSE 80