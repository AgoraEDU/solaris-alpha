# Solaris Alpha - Client Management System

[![Docker](https://img.shields.io/badge/-Docker-black?style=flat&logo=docker&logoColor=2496ED)]()
[![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=python&logoColor=FFD43B)]()
[![MySQL](https://img.shields.io/badge/-MySQL-black?style=flat&logo=mysql&logoColor=00758F)]()
[![License](https://img.shields.io/badge/-AGPL-black?style=flat&logo=gnu&logoColor=A42E2B)]()
[![Code Style](https://img.shields.io/badge/-Code%20Style-black?style=flat&logo=codefactor&logoColor=A42E2B)](https://google.github.io/styleguide/pyguide.html)

## Description

Solaris Alpha is a client management system with a focus on simplicity and ease-of-use, the application is
designed to work with MySQL databases, being able to evaluate and filter client data exposed by
the application.

> [!WARNING] 
> This application is still in development and undergoing rigorous testing. It will be
> released as a beta version once it is fully tested and when we believe it is at its
> best state.

## Table of Contents
 
- [Installation](#installation)
- [License](#license)
- [Contributions](#contributions)

## Installation

To get started, first clone the repository and install the required dependencies:
```bash
git clone https://github.com/AgoraEDU/solaris-alpha.git . && pip install -r requirements.txt
```

> NOTE: You could also just use the Docker image we will provide in the future.

Once the dependencies are installed, you can run the application using the following command:

```bash
py | python main.py --sc --cts --db --host --port --user --password
```

From here, you can start using the application since its using nicegui to create a user interface.

> [!WARNING]
> All options are subject to change, so please use the options above to configure the application.
> We may also add more options in the future which may or may not remove previous options.

Each of the arguments specified below are optional, however, it makes it easier to run the application with
an environment that you have configured beforehand.

### Options

| Option       | Description                               | Default   |
|--------------|-------------------------------------------|-----------|
| `--sc`       | Enables the Solaris Clients module        | False     |
| `--cts`      | Enables the Client Tracking System module | False     |
| `--db`       | Enables the Database module               | False     |
| `--host`     | The host of the database                  | localhost |
| `--port`     | The port of the database                  | 3306      |
| `--user`     | The user of the database                  | root      |
| `--password` | The password of the database              | root      |

> NOTE: The database module is not enabled by default, and it's going to solely rely on .json files stored locally from
> a specific file path.

## License

This project is licensed under the GNU Affero General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Contributions





