from django.core.management.base import BaseCommand
from django.db import transaction

from sampledatahelper.helper import SampleDataHelper

from cinemair.users.models import User
from cinemair.cinemas.models import Cinema
from cinemair.movies.models import Movie
from cinemair.shows.models import Show
from cinemair.events.models import Event

NUM_USERS = 9
NUM_SHOWS = 400
RANGE_EVENTS = [3, 8]
MOVIES_IDS = [157336, 155, 98, 76341, 278, 238, 600, 78, 935, 185, 539, 346, 289, 389, 914, 5156, 653, 626, 19]

CINEMAS = [
    ("The Urban Beach Cinema Conde Duque", "Conde Duque, 11"),
    ("Sunset Cinema", "Plaza de Cibeles"),
    ("Parque de la Bombilla", "Av. De Valladolid"),
    ("Auditorio Parque Calero", "Calle José del Hierro"),
    ("Cine Doré", "Santa Isabel, 3"),
    ("La Casa Encendida", "Ronda de Valencia, 2"),
    ("Cine en el paraíso", "Parque el Paraíso"),
]

class Command(BaseCommand):
    sd = SampleDataHelper(seed=1234567890)

    @transaction.atomic
    def handle(self, *args, **options):
        # Create admin user
        self._create_admin_user()

        # Create cinemas
        for name, address in CINEMAS:
            self._create_cinema(name, address)

        # Create movies
        for i in MOVIES_IDS:
            self._create_movie(i)

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

    def _create_cinema(self, name, address):
        return Cinema.objects.create(name=name,
                                     address=address,
                                     city="Madrid",
                                     country="Spain")

    def _create_movie(self, id):
        return Movie.objects.create(name=self.sd.words(1, 5),
                                    tmdb_id=id)

    def _create_show(self):
        return Show.objects.create(movie=self.sd.db_object(Movie),
                                   cinema=self.sd.db_object(Cinema),
                                   datetime=self.sd.future_datetime(max_distance=60*24*90))


    def _create_event(self, user, show):
        return Event.objects.create(user=user, show=show)
