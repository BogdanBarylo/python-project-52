### Hexlet tests and linter status:
[![Actions Status](https://github.com/BogdanBarylo/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/BogdanBarylo/python-project-52/actions)
[![Python CI](https://github.com/BogdanBarylo/python-project-52/actions/workflows/github_actions.yml/badge.svg)](https://github.com/BogdanBarylo/python-project-52/actions/workflows/github_actions.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/db3c5ac363e7706ece1e/test_coverage)](https://codeclimate.com/github/BogdanBarylo/python-project-52/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/db3c5ac363e7706ece1e/maintainability)](https://codeclimate.com/github/BogdanBarylo/python-project-52/maintainability)

# Task Manager

## Usage
Task Manager is a task management system. It allows you to set tasks, assign executors and change their statuses.
To use the application, you need to register and log in with your username and password.
A registered user can create, modify and delete tasks, statuses and labels. A task can be deleted only by its author.
The project implements translation into 2 languages. By default Russian is set, but if you need to use English you need to set in settings.py 
LANGUAGE_CODE = 'en'

### View site here:
[Task Manager](https://task-manager-site-tpi0.onrender.com)


## Installation requirements

- Python: 3.10
- Poetry: 1.4.0

#### Repository cloning
```bash
git clone git@github.com:BogdanBarylo/python-project-52.git
cd python-project-52
```

#### Installing dependencies

```bash
make install
```

#### Installation instructions

To get started, you need to create a database and specify its **DATABASE_URL** in the task_manager/settings.py file of your project. In addition, you should define your **SECRET_KEY** in the same file. I used SQLite locally in my project, and PostgreSQL when I deployed it.
```bash
DATABASE_URL='sqlite:///task_manager.sqlite3'
SECRET_KEY='{your secret key}'
```

#### Migrations
```bash
make build
```
#### Local use

```bash
make dev
```

## Contributions

Contributions to the Task Manager project are always welcome! If you encounter any issues or have suggestions for enhancements, please submit an issue or pull request. 