# simpleCRM

## Setup

    npm install
    bower install
    mkvirtualenv -p python3.5 <env_name>
    pip3 install -r requirements.txt

## Database

    sudo -i -u postgres
    psql
    create user <username> with password "<password>";
    create database <database_name>;
    grant all privileges on database <database_name> to <username>;
