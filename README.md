# simpleCRM

## Setup

    npm install
    bower install
    mkvirtualenv -p python3.5 <env_name>
    pip3 install -r requirements.txt

    ## add GOOGLE_MAP_KEY to environment variables
    echo "export GOOGLE_MAP_KEY = <KEY>" >> ~/<virtualenv_path>/<env_name>/bin/postactivate

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver 

## Database

    sudo -i -u postgres
    psql
    create user <username> with password "<password>";
    create database <database_name>;
    grant all privileges on database <database_name> to <username>;
