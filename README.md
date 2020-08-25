# gift-exchange-app

## Development

1. Clone repo

   ```shell
   git clone git@github.com:charwking/gift-exchange-app.git
   ```

1. Install `poetry`

   ```shell
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
   ```

1. Change directory into the git repo
    ```shell
    cd gift-exchange-app
    ```

1. Create a virtual environment dedicated to this app

   ```shell
   python3 -m venv --prompt=gift .venv
    ```

1. Activate your virtual environment

   ```shell
   source .venv/bin/activate
   ```

1. Install dependencies within your activated environment

   ```shell
   poetry install
   ```

1. To run tests

   ```shell
   TODO
   ```

1. To run application

   ```shell
   TODO will be using uvicorn
   ```

## TODO

* Clean up TODOs
* Add auto-formatting with Black
* Add GitHub actions for executing tests, Black, etc?
* Figure out deploying and running in dev environment
* Add GitHub action for deploys to dev environment?
* Talk to a DB
