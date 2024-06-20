FROM node:18.20.2

WORKDIR /app


RUN apt-get update -qq && yarn global add @vue/cli
RUN npm install yarn


COPY .. :
RUN yarn
CMD ["yarn", "dev", "--port", "3030"]