from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Crear usuarios
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel.name),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc.name),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc.name),
        ]

        # Crear actividades
        Activity.objects.create(user=users[0].name, type='run', duration=30)
        Activity.objects.create(user=users[1].name, type='bike', duration=45)
        Activity.objects.create(user=users[2].name, type='swim', duration=25)
        Activity.objects.create(user=users[3].name, type='yoga', duration=60)

        # Crear leaderboard
        Leaderboard.objects.create(user=users[0].name, points=100)
        Leaderboard.objects.create(user=users[1].name, points=80)
        Leaderboard.objects.create(user=users[2].name, points=120)
        Leaderboard.objects.create(user=users[3].name, points=90)

        # Crear entrenamientos
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Plank', description='Hold plank for 1 minute')
        Workout.objects.create(name='Squats', description='Do 30 squats')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
