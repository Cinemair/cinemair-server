from django.core.management.base import BaseCommand
from django.db import transaction

from sampledatahelper.helper import SampleDataHelper

from cinemair.users.models import User
from cinemair.cinemas.models import Cinema
from cinemair.films.models import Film
from cinemair.shows.models import Show


NUM_CINEMAS = 6
NUM_FILMS = 10
NUM_SHOWS = 100


class Command(BaseCommand):
    sd = SampleDataHelper(seed=1234567890)

    @transaction.atomic
    def handle(self, *args, **options):
        # Create admin user
        self._create_admin_user()

        # Create cinemas
        for i in range(1, NUM_CINEMAS + 1):
            self._create_cinema()

        # Create films
        for i in range(1, NUM_FILMS + 1):
            self._create_film()

        # Create shows
        for i in range(1, NUM_SHOWS + 1):
            self._create_show()

    def _create_admin_user(self):
        user = User.objects.create(username="admin",
                                   email="admin@cinemair.com",
                                   full_name="Administrator")

        user.set_password("123123")
        user.save()
        return user

    def _create_cinema(self):
        return Cinema.objects.create(name=self.sd.words(1, 3))

    def _create_film(self):
        return Film.objects.create(name=self.sd.words(1, 5))

    def _create_show(self):
        return Show.objects.create(film=self.sd.db_object(Film),
                                   cinema=self.sd.db_object(Cinema),
                                   datetime=self.sd.future_datetime(max_distance=60*24*90))


