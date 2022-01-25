# - Hidden Words Generator -
Hidden Words generator is a web-app that will allow you to download a 
hidden words PDF grid. This game has many names, so I'll 
simply explain it to you in case you don't know what it is: 
you have an X * X grid where letters are placed at each position. 
In this mess, you have to find words by vertical, horizontal or diagonal. 
The words list can be found just below the grid in the PDF.
FYI, my version is in French! But you can easily make your own
with my code by scraping another dictionary or bringing your own
list of words.

## Link to website
http://hidden-words.fr/ (might be broken depending on when you are
looking at this project. You can see the website visual below).
You will need to activate pop-up to be able to download a PDF.

## How to install on your own
Everything can be found in the docs folder. You have many documents
that covers all the information about the app. Including the one regarding
the deployment. I did everything with AWS DynamoDB, S3, Lambda and API Gateway,
so the docs only shows this solution. Feel free to use another method.
Sorry the documentation is also in French, but it wouldn't be hard to
understand as commands are still in english, and I redirect to some AWS docs.

Doc files are :

- Functional brief: the app overall and his actors are described
- Technical brief: we dive deeper in what the app is made of (aws structure)
- Deployment brief: everything you need to know on how to install the app on your own

## Flake8
The app is fully flake8 compliant. You can run it with:
`flake8`

## Pytest Coverage
Pytest coverage score is at 90%. You can run it with:
- `coverage run -m pytest`
- `coverage html` (an html report will be created in your project root folder)

## App screenshot
![example](https://github.com/bientavu/hidden_words/blob/master/website/assets/img/app-screenshot-blur.png?raw=true)
