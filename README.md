# Knights Heroku-Django-View-Integration

## What this is.

I always figured the Heroku logo looks like a castle tower, and python is snakes, so here is Knights, an integration template for a heroku-deployed, integrated django and vue project. See a small-scale app using this structure here: https://medknights.herokuapp.com 

# It takes two seconds to load, warning: German language! 

> The linked prokect is not the base template found in this repo, but an implementation.

Added on top is simply a user signup system (django standard user admin), and once you login as a user you have access to the Vue app. Neat! This gives you a sense of where you can take this base template, but the core idea is a responsive Vue SPA framed by the utility of Django.

## And how to do it.

The core steps are the ones found in the Heroku docs on django. 

For a great write-up, here is William Lee over at Medium with the same basic idea and great steps to follow.

https://medium.com/@williamgnlee/simple-integrated-django-vue-js-web-application-configured-for-heroku-deployment-c4bd2b37aa70

> At the point of writing, the Medium is about three years out of date, and the Heroku docs are a bit older even. The rest of this Readme concerns itself with the most important codebase changes to be weary of, as implemented in this repo.

In addition, the Lee piece does not cover database setup, which we will do here: the medknights example above uses Postgres, and that's the template choice as well.

So before we begin, here is our toolkit for today:

- Django and Vue
- Node.js, npm
- axios
- django-cors-headers
- and Postgres for db

In order, here are the steps in the Lee that need modification in 2021(+).

...



