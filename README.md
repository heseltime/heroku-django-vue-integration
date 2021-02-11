# Knights Heroku-Django-View-Integration

## What this is :question:

:european_castle: :heavy_plus_sign: :snake: ...

I always figured the Heroku logo looks like a castle tower, and python is snakes, so here is Knights, an integration template for a heroku-deployed, integrated django and vue project. See a small-scale app using this structure here: https://medknights.herokuapp.com 

# It takes two seconds to load, warning: German language! 

> The linked prokect is not the base template found in this repo, but an implementation.

# Here is the template in action: https://heroku-django-vue.herokuapp.com/#/

> Takes two seconds to load (Heroku).

Added on top in the first example is simply a user signup system (django standard user admin), and once you log in as a user you have access to the Vue app. Neat! This gives you a sense of where you can take this base template, but the core idea is a responsive Vue SPA framed by the utility of Django. The core piece is a Django API (a view that implements a JSON set) that is then consumed by Vue with the help of Axios.

## And how to do it :rocket:

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
- oh and also because I like to use Fontawesome in ALL my projectsw, vue-fontawesome: https://github.com/FortAwesome/vue-fontawesome

> This is a great template to get into muscle memory, as it is a super base for all kinds of projects, typically from a small to medium scale.

In order, here are the numbered steps in the Lee we want to modify a bit:

### Step 1 is straigtforward, Step 2 required the following modification using Venv as my virtual environments tool (Lee uses Conda) and regular npm.

> In Venv: 

    npm install -g @vue/cli

and

    vue init webpack .
    
 The dot targets the same directory. I like the structure Lee uses, vue sitting directly inside the Django structure.
 
 ### Step 3
 
 Don't forget to 
 
     import os
     
 Duh, but Lee doesn't mention
 
 ### Next steps are straighforward, Step 8 however:
 
 Two pieces here.
 
A) 

The latest version of WhiteNoise removes some options which were deprecated in the previous major release: The WSGI integration option for Django (which involved editing wsgi.py) has been removed. Instead, you should add WhiteNoise to your middleware list in settings.py and remove any reference to WhiteNoise from wsgi.py. 

B) 

The whitenoise.django.GzipManifestStaticFilesStorage alias has now been removed. Instead you should use the correct import path: whitenoise.storage.CompressedManifestStaticFilesStorage.

See also: http://whitenoise.evans.io/en/stable/changelog.html#v4-0

Overlooking this part can result in errors like

    The resource from “https://heseltime.herokuapp.com/static/css/app.48175cc56e52e020bf178616c0977374.css” was blocked due to MIME type (“text/html”) mismatch (X-Content-Type-Options: nosniff).
    
### The final steps are also still up to date.

And I absolutely love the deploy via Github option Heroku provides!

## The rest of this setup/readme concerns Postgres setup.

This is not covered in the Lee guide, so I'll go into it one by one.

### 1


