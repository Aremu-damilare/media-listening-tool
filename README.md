## What's media listening tool
A media listening tool allow users to monitor and analyze certain keywords they searched for.

## About this app
This web app is built using django and django rest framework. Its inspired by mediatoolkit,
it takes keywords from users and scrapes certain websites for data/comments/reviews/tweets 
relating to the keyword.

This app itself doesn't scrap the internet for data, that is done with NodeJS,
it only sends request to the nodejs server to scrap for data and send back to this app database.

### Features
1. Auto scrap for data at interval
2. Perform analysis on the scrap data
3. Notify users of new data scrap
4. Users can perform advanced search 



# ! The app is still being developed....

You can send pull request and raise issues, Thank you.
**Note**: This project doesnt intent to have a UI,just endpoints.