<a  href="https://www.twilio.com">
<img  src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg"  alt="Twilio"  width="250"  />
</a>
 
# CovidAssist

## About

This is A COVID-19 Assist applications that tells people what the recovered, death and confirmed cases are in their respective countries
It is still a work in progress but works well.

### How it works

- I have writted a flask web service which interacts with the covidapi.info api to get data on countries.
- I am using pycountries to fuzzy search country ISO when someone types in a country.
- I am using twiml and whatsapp sandbox to interact with users. (twilio api).
- I am using heroku for deployment of my flask web service.

## Features

- Information about All countries and their Covid Count.
- Updated and Accurate information as well as request caching to enable faster response times. 

## Set up and Use

- Add number : +1 415 523 8886
- Send text to join sandbox : join fellow-image
- Send text to get information about country: Information USA 
- examples: Information USA / Information India / Information China / information Pakistan 

<img  src="https://res.cloudinary.com/practicaldev/image/fetch/s--DXzqOVdL--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/hap7eobtxpqvdmqctaje.png"/>
<img src = "https://res.cloudinary.com/practicaldev/image/fetch/s--CKyzGNGm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/chuaivgcbo5xsiv5ywqo.png" />

### Requirements

- a whatsapp number

### Twilio Account Settings

Setup a whatsapp sandbox in by creating a free twilio account.

### Local development

After the above requirements have been met:
 -  Clone this repo 
 -  setup a virtual environment using pip3 install virtualenv
 -  install dependencies in requirements.txt pip3 install -r requirements.txt
 -  run python3 app.py and expose localhost using ngrok / or deploy using heroku
 -  use sandbox and setup whatsapp bot
 -  (follow the above steps by adding number and joining sandbox) Done

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.

[twilio]: https://www.twilio.com
