# offerings_be

[![Build Status](https://travis-ci.org/Ajshannon/offerings_be.svg?branch=master)](https://travis-ci.org/Ajshannon/offerings_be)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

a restful django app for Offerings. Check out the project's [documentation](http://Ajshannon.github.io/offerings_be/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/)
- [Heroku Toolbelt](https://toolbelt.heroku.com/)

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Continuous Deployment

Deployment is automated via Travis. When builds pass on the master or qa branch, Travis will deploy that branch to Heroku. Follow these steps to enable this feature.

Initialize the production server:

```
heroku create offerings_be-prod --remote prod && \
    heroku addons:create newrelic:wayne --app offerings_be-prod && \
    heroku addons:create heroku-postgresql:hobby-dev --app offerings_be-prod && \
    heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="offerings_be-prod" \
        DJANGO_CONFIGURATION="Production" \
        DJANGO_SETTINGS_MODULE="offerings_be.config" \
        --app offerings_be-prod
```

Initialize the qa server:

```
heroku create offerings_be-qa --remote qa && \
    heroku addons:create newrelic:wayne --app offerings_be-qa && \
    heroku addons:create heroku-postgresql:hobby-dev --app offerings_be-qa && \
    heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="offerings_be-qa" \
        DJANGO_CONFIGURATION="Production" \
        DJANGO_SETTINGS_MODULE="offerings_be.config" \
        --app offerings_be-qa
```

Securely add your Heroku credentials to Travis so that it can automatically deploy your changes:

```bash
travis encrypt HEROKU_AUTH_TOKEN="$(heroku auth:token)" --add
```

Commit your changes and push to master and qa to trigger your first deploys:

```bash
git commit -a -m "ci(travis): add Heroku credentials" && \
git push origin master:qa && \
git push origin master
```

# Testing

To run pytest, run 'docker-compose run web pytest -v' twice in your terminal.  The first run is required to build the test db.

Occassionally a postgres error will occur if docker-compose is run many times.  In this case, please run
'docker kill $(docker ps -q) && docker rm $(docker ps -a -q) && docker-compose build.

You're now ready to continuously ship! ✨ 💅 🛳


