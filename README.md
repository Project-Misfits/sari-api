## Sari-sari Store Backend API
version 1.0

### Running locally
- Requires python 3.X

* Install dependencies listed in requirements.txt with command 
`pip install -r requirements.txt`
* Rename `sari-api/.env.example` to `sari-api/.env` and update settings
* python makemigrations
* python migrate
* python manage.py runserver

### Testing
- Coding Style
[PEP8](https://peps.python.org/pep-0008/ "PEP8") is enforced for coding style using Flake8. To check for coding style errors simply use the command `flake8` while inside the root folder.
