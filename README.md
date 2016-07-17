# Cinemair
### A Madrid open air cinema movie finder mobile app

![Cinemair](http://i.imgur.com/4wG4niB.png)


#### Install (develop env.):

  ```
  mkvirtualenv -p /usr/bin/python3 cinemair
  pip install -r requirements-devel.txt

  # Use --from-fixtures if you want more realistic dates
  ./scripts/regenerate.sh

  ./manage.py runserver
  ```
