FROM node:18.20.2

WORKDIR /app

# RUN npm init -y
# RUN npm install -g npm
# RUN apt-get update -qq && npm install -g vue-cli

# COPY .. :

# ENTRYPOINT ["npm", "run", "dev"]

RUN apt-get update -qq && yarn global add @vue/cli
RUN npm install yarn


COPY .. :
RUN yarn
CMD ["yarn", "dev", "--port", "3000"]