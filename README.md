# Install

## Run docker compose
```bash
docker compose up -d
```

## Install pip packages
```bash
pip install -r requirements.txt
```

## Load fixtures data
```bash
python manage.py loaddata users
python manage.py loaddata helpers
python manage.py loaddata categries
python manage.py loaddata content
```

## Load post data
```bash
python manage.py load_yozing
```


## Remove post data
```bash
python manage.py remove_yozing
```