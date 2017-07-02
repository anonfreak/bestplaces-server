[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7f10b5a255ba4b1cb7ec9494b6f29c7c)](https://www.codacy.com/app/kolb.marco/bestplaces-server?utm_source=github.com&utm_medium=referral&utm_content=anonfreak/bestplaces-server&utm_campaign=badger)
[![Build Status](https://travis-ci.org/anonfreak/bestplaces-server.svg?branch=master)](https://travis-ci.org/anonfreak/bestplaces-server)
[![Coverage Status](https://coveralls.io/repos/github/anonfreak/bestplaces-server/badge.svg?branch=master)](https://coveralls.io/github/anonfreak/bestplaces-server?branch=master)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/heroku/node-js-sample)
# BestPlaces
Track your favorite Places and find more of them.
## Structure
Because of our Server-Client-Structure, we decided to use two different repositories to devide server and client, which both are written in different languages. You are able to access our client-repository [here](http://github.com/anonfreak/bestplaces-client).
## Idea
Our server will be able to communicate with clients by using a RESTful API, developed with Python. Therefore, we use Django to provide our own API.


## Installation
Now it comes to install our application on your server. Maybe you recognized the "Deploy to Heroku Button" at the top of this README, which allows you to deploy our application with a click of a button (and small sign-up on Heroku). But first, you'll need an API Key for the Google Places API, which is needed for our Application. Therefore follow this [Guide](https://developers.google.com/places/web-service/get-api-key?hl=de) from Google.
After you've created your API key, just klick the button on the top and edit the Environment-Variable-Field "PLACES_API_KEY" with your API Key. Then give your application a name and click on "deploy". Now Heroku will automatically deploy our Application to your Heroku server.
