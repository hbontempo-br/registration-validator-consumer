# registration-validator-consumer
A CLI tool to consume [hbontempo-br/registration-validator-api](https://github.com/hbontempo-br/registration-validator-api)
***

## API Install Guide

*This project is meant to run using **python 3.7** in an Unix-like system , other versions and OSs may not work.*

All dependencies are listed on requirements.txt file. Its strongly recommended to run service in a virtual environment.

### Clone project
```sh
$ git clone git@github.com:hbontempo-br/registration-validator-consumer.git
```

### Setup a Virtual Environmnet
For linux/Debian distros:
```sh
$ sudo apt-get python3-venv
$ python3 -m venv .venv
$ source .venv/bin/activate
```
#### Install dependencies

From inside the project's folder:

```sh
$ pip3 install -r requirements.txt
```

#### Environment Variables

This project requires this environment variables:

| Variable | Definition | Example | Default |
| - | - | - | - |
| URL | The address of application your hbontempo-br/registration-validator-api | http://0.0.0.0:3001 | http://0.0.0.0:3001 |

## What you can do?

If you are not sure what it does: 
```sh
$ python3 register-validator-consumer.py
Usage: register-validator-consumer.py [OPTIONS] COMMAND [ARGS]...

  Registration Validation Consumer- A small CLI made with a simple reason:
  consume hbontempo-br/register-validator-api

Options:
  --help  Show this message and exit.

Commands:
  register  Register a new person
  search    search new person through it`s social_security_number
```

Register a new person:
```sh
$ python3 register-validator-consumer.py register
A small CLI made with a simple reason: hbontempo-br/register-validator-api

Please provide the person`s information.
First name: Test  
Last name: Person
Phone [format - (xx)xxxxxxxxx]: (11)87878787
Social security number (only numbers): 93823118072

Registering...

Ok. Person registered.
```

Retrieve a person's register
```sh
$ python3 register-validator-consumer.py search 93823118072
A small CLI made with a simple reason: hbontempo-br/register-validator-api

Searching tor registration.

Person found.
first_name: Test
last_name: Person
phone: (11)87878787
social_security_number: 93823118072
success: True
```

## Contributing

This project has a strict formatting validation, but it's super easy to adhere to. Just use the automatic pre-commit.

### Install the pre commit:

From inside the project's folder:

Make sure the dependencies refereed on requirements-dev.txt are installed:

```sh
$ pip3 install -r requirements-dev.txt
```

Install the pre-commit:

```sh
$ pre-commit install
```

### Using it:

Just make a commit! On every commit now on all the super strict formatting is taken care of automagically.

If you want to run the validation without a commit just run:
```sh
$ pre-commit run --all-files
```


<br/>
<br/>
<br/>

---

