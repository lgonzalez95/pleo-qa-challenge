# pleo-qa-challenge

Challenge for Pleo.io QA position

<img src="https://upload.wikimedia.org/wikipedia/commons/4/48/Twelve_Labours_Altemps_Inv8642.jpg" height="300px"/>

## The challenge: Money Formatting

Given an amount of money as a number, format it as a string. Add associated tests for the functionality and for the user interface. 

```js
formatMoney(2310000.159897); // '2 310 000.16'
formatMoney(1600); // '1 600.00'
```

## My approach

I decided to take this challenge as a `real life use case` - in other words if I were hired to develop and test the solution I would do exatly the same code as I am delivering for this challenge.

Despite the fact that I was encouraged and tempted to use Kotlin or Typescript I decided to code my solution on Python3 cause I feel more confortable with it. I wanted to demostrate solid testing principles and a good testing strategy and I didn't want time or techonlogy to hold me back, so I developed in the language I could spent less time researching and more time developing.

## My solution

I created a simple web application using Flask that just renders 2 pages (index, and 404). There is a function inside `flaskr/core/money.py` that handles the formatting of the given value, the rest of the code is flask related code to properly handle the app routing.

Why a webapp? Having a minimalistic application really simplifies the testing process. The solution has a high level of coverage for both unit (+86%) and e2e testing, and because there are no un-needed components by extension there are no un-needed tests.

I created an application that can be easily tested at unit and e2e levels, all the code is on the same repository and uses the same language in order to simplify the ci/cd process.

## E2E Testing with Playwright

`Playwright` is a modern e2e testing framework created and open sourced by Microsoft that is quickly becoming the strongest competitor for Webdriver. It is supper fast compared to webdriver and has also cross-browser support which pushes other competitors away of the fight. I decided to use for this exercise because I felt it is stable enough for a production application, also it is very easy yo setup and run with its own pytest plugin.

## CI/CD
I decided to use `github actions` because it can easily be setup and integrated on the same repository (no extra dependencies or third party tools are required).

There are only 2 steps for each of the testing levels that are supported.
[Actions](https://github.com/pjcalvo/pleo-qa-challenge/actions)

###### Tech Stack
* Python3
* Flask (WebApp)
* Pytest (unit testing)
* Pytest + Playwright (e2e testing)

## Setting up the environment:
###### Python3
It is used to run and test the API as well as to run the front end app.

* If you are in a mac simple: `brew install python3`
* If not or you don't have brew installed follow this [Python3](https://www.python.org/downloads/)

## Setting up the project
Once we have the environment ready we need to install the project dependencies:
*At this point I am assuming you already cloned the repo*

**Python** recommendation is to use a virtual env when installing dependencies to avoid conflict with OS libraries
`python3 -m venv venv` create the virtual env
`. venv/bin/activate` source to the virtual env, you will see (venv) in the terminal
`pip install -r requirements.txt` install project dependencies
`python -m playwright install` install browser dependencies

## Running the project
There is a `Makefile` to simplify the executions.

###### WebAPP
Open the terminal and run: `make run`
Check the [app](http://localhost:8080)

###### Unit Testing
This solution contains 3 levels of testing:
###### Unit testing
* Make sure you are in the virtual env all the time`. venv/bin/activate`
* To execute the tests simple run `make tests-unit` which will find all the pytest methods under the folder and run them.

Note: I added a test that handles the big list of nasty strings input and check that the result is a *type(str)* which means that it doesn't broke

###### E2E Tests | Acceptance Tests | UI Tests

You can call these guys *e2e tests*, *acceptance tests*, *ui tests* or whatever seems right on the context, they are the last level of testing that I added, like the cherry on the cake.

In this case I decided to use [Playwright](https://github.com/microsoft/playwright-python) because it is a fast modern framework that just make e2e testing very simple. It does not require a webdriver instance to run.

To run the acceptance tests we need a working webapp, so:

* In a terminal: Move to the virtual env: `. venv/bin/activate` then spin up the webapp `make run`
* In a second terminal: Move to the virtual env: `. venv/bin/activate` then run the tests `make tests-e2e`. They run by default on headless mode, if you want to execution then instead run `tests-e2e-headful`.

That is it for the testing.


## Continues Integration and Testing
This solution includes support for CI/CT using `github actions` but is not deployed anywhere.

The pipeline is structured to:

* Run the unit tests with code coverage and upload a report
* Run the e2e coverage by spinning the webapp and execution the tests.

Also, this runs over every commit or PR that is done to *Main*. In a better process I will split the process differently, we need to consider a pipeline for each one of the microservices and also a different pipeline to tests UI tests on top of everything maybe after each service is deployed to Staging environment we need to identify if at this level the machine is still running.


## Notes on what I didn't do? What I would do different? What would I like to include if I had more time!?

**What I didn't do?**
I didn't consider to add any *performance or load testing*. I consider load testing as a driven context effort and in this case the context of having a single page hitting a single endpoint with no real customers is not worth the effort. Performance testing is meant to find software, infraestructure, network and db bottlenecks, but this app is not even deployed so performance testing will not make a lot of sense.

I didn't add visual UI verification because the application is just a button; but if we wanted it we could have done that using Applitools or other Python image processing library to record baselines and compare against new tests.

I didn't add any automated security testing, same as performance testing there is a big effort that needs to be invested here but no security at all on the site so I didn't think it was worth it.


**What would I like to include if I had more time!?**

* More coverage for negative tests on the front end. What happens if the webapp get stuck or is too slow?
* Better reporting and logging tools for the tests, right now it is mostly console reports, but this does not provide an easy way to debug or troubleshoot in case of errors. Including attached screenshots and logs to the execution.

**What is next?**
I didn't explain a lot the technical details of the proyect. I would love to sit with the Pleo employess that are in charge or reviewing my application and discuss further deep on my solution.

Happy reviewing! 🚀
