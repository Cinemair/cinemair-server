#!/bin/bash
#!/bin/bash

python ./manage.py dumpdata --format json \
                            --indent 4 \
                            --output './cinemair/fixtures/initial_data.json' \
                            'cinemas.Cinema' \
                            'movies.Movie' \
                            'shows.Show'
