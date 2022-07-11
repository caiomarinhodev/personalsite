from django.core.management.base import BaseCommand, CommandError
from django_crud_generator.django_crud_generator import copy_deps


class Command(BaseCommand):
    help = 'Generate files by models'

    def add_arguments(self, parser):
        parser.add_argument('--app', action='store', type=str)

    def handle(self, *args, **kwargs):
        try:
            print('-- Copy requirements, procfile, and CI file')
            copy_deps()
        except (Exception,):
            raise CommandError('Error, try again.')
