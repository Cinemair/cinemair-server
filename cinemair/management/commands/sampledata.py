from django.core.management.base import BaseCommand
from django.db import transaction

from sampledatahelper.helper import SampleDataHelper

from cinemair.users.models import User
from cinemair.cinemas.models import Cinema
from cinemair.films.models import Film
from cinemair.shows.models import Show
from cinemair.events.models import Event

NUM_USERS = 9
NUM_CINEMAS = 6
NUM_FILMS = 10
NUM_SHOWS = 400
RANGE_EVENTS = [3, 8]


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

        # Create users
        for i in range(1, NUM_USERS + 1):
            self._create_user(i)

        # Create events
        for user in User.objects.all():
            shows = Show.objects.all()
            for i in range(self.sd.int(RANGE_EVENTS[0], RANGE_EVENTS[1])):
                show = self.sd.db_object_from_queryset(shows)
                self._create_event(user, show)
                shows = shows.exclude(id=show.id)


    def _create_admin_user(self):
        user = User.objects.create(username="admin",
                                   email="admin@cinemair.com",
                                   full_name="Administrator",
                                   is_superuser=True)

        user.set_password("123123")
        user.save()
        return user

    def _create_user(self, id):
        user = User.objects.create(username="user{}".format(id),
                                   email="user{}@cinemair.com".format(id),
                                   full_name="{} {}".format(self.sd.name('es'),
                                                            self.sd.surname('es', number=1)))

        user.set_password("123123")
        user.save()
        return user

    def _create_cinema(self):
        return Cinema.objects.create(name=self.sd.words(1, 3),
                                     address="{}, {}".format(self.sd.words(1, 3), self.sd.int(1, 200)),
                                     city="Madrid",
                                     country="Spain")

    def _create_film(self):
        return Film.objects.create(name=self.sd.words(1, 5))

    def _create_show(self):
        return Show.objects.create(film=self.sd.db_object(Film),
                                   cinema=self.sd.db_object(Cinema),
                                   datetime=self.sd.future_datetime(max_distance=60*24*90))


    def _create_event(self, user, show):
        return Event.objects.create(user=user, show=show)
