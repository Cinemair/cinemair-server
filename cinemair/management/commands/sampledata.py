from django.core.management.base import BaseCommand
from django.db import transaction

from sampledatahelper.helper import SampleDataHelper

from cinemair.users.models import User
from cinemair.cinemas.models import Cinema
from cinemair.movies.models import Movie
from cinemair.shows.models import Show
from cinemair.favorites.models import Favorite

NUM_USERS = 9
NUM_SHOWS = 400
RANGE_EVENTS = [3, 8]
MOVIES_IDS = [157336, 155, 98, 76341, 278, 238, 600, 78, 935, 185, 539, 346, 289, 389, 914, 5156, 653, 626, 19, 11042, 773, 20607, 575, 31175]

CINEMAS = [
    ("Cine de verano de Malasaña", "Calle Antonio Grilo, 8", 8.00),
    ("The Urban Beach Cinema Conde Duque", "Conde Duque, 11", 6.50),
    ("Sunset Cinema", "Plaza de Cibeles", 1.20),
    ("Parque de la Bombilla", "Av. De Valladolid", 0.00),
    ("Auditorio Parque Calero", "Calle José del Hierro", 4.50),
    ("Cine Doré", "Santa Isabel, 3", 3.65),
    ("La Casa Encendida", "Ronda de Valencia, 2", 2.80),
    ("Cine en el paraíso", "Parque el Paraíso", 4.99),
]

class Command(BaseCommand):
    help = 'Populate an empty database with data for development purpose.'
    sd = SampleDataHelper(seed=1234567890)

    def add_arguments(self, parser):
        parser.add_argument(
            "--from-fixtures",
            action="store_true",
            dest="from-fixtures",
            default=False,
            help="Load more real dates from a fixture (default false)",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        # Create admin user
        self.stdout.write(" -> Create admin user [ username: 'admin' | password: '123123' ]. ")
        self._create_admin_user()

        if options["from-fixtures"]:
            self.stdout.write(" -> Load data from fixtures.")
            self._populate_with_fixtures()
        else:
            self.stdout.write(" -> Generate sample data.")
            self._populate_with_sampledata()

    def _populate_with_fixtures(self):
        from django.core.management import call_command
        call_command("loaddata", "initial_data", traceback=True)

    def _populate_with_sampledata(self):
        # Create cinemas
        for name, address, price in CINEMAS:
            self._create_cinema(name, address, price)

        # Create movies
        for i in MOVIES_IDS:
            self._create_movie(i)

        # Create shows
        for i in range(1, NUM_SHOWS + 1):
            self._create_show()

        # Create users
        for i in range(1, NUM_USERS + 1):
            self._create_user(i)

        # Create favorites
        for user in User.objects.all():
            shows = Show.objects.all()
            for i in range(self.sd.int(RANGE_EVENTS[0], RANGE_EVENTS[1])):
                show = self.sd.db_object_from_queryset(shows)
                self._create_favorite(user, show)
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

    def _create_cinema(self, name, address, approximate_price):
        return Cinema.objects.create(name=name,
                                     address=address,
                                     approximate_price=approximate_price,
                                     city="Madrid",
                                     country="Spain")

    def _create_movie(self, id):
        return Movie.objects.create(name=self.sd.words(1, 5),
                                    tmdb_id=id)

    def _create_show(self):
        return Show.objects.create(movie=self.sd.db_object(Movie),
                                   cinema=self.sd.db_object(Cinema),
                                   datetime=self.sd.future_datetime(max_distance=60*24*90))


    def _create_favorite(self, user, show):
        return Favorite.objects.create(user=user, show=show)
