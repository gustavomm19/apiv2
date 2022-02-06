import os, requests, logging
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from ...actions import create_asset
from ...models import AssetAlias

logger = logging.getLogger(__name__)

HOST_ASSETS = 'https://assets.breatheco.de/apis'


class Command(BaseCommand):
    help = 'Sync exercises and projects from old breathecode'

    def add_arguments(self, parser):
        parser.add_argument('entity', type=str)
        parser.add_argument(
            '--override',
            action='store_true',
            help='Delete and add again',
        )
        parser.add_argument('--limit',
                            action='store',
                            dest='limit',
                            type=int,
                            default=0,
                            help='How many to import')

    def handle(self, *args, **options):
        try:
            func = getattr(self, options['entity'], 'entity_not_found')
        except TypeError:
            print(f'Sync method for {options["entity"]} no Found!')
        func(options)

    def _exists(self, slug):
        aa = AssetAlias.objects.filter(Q(slug=slug) | Q(asset__slug=slug)).first()
        return aa is not None

    def exercises(self, options):
        response = requests.get(f'{HOST_ASSETS}/registry/all')
        items = response.json()
        for slug in items:
            if self._exists(slug) and options['override'] == False:
                print('Skipping: Asset with this alias ' + slug + ' already exists, use the')
                continue
            data = items[slug]
            if 'grading' in data:
                data['graded'] = data['grading']

            create_asset(data, asset_type='EXERCISE', force=(options['override'] == True))

    def projects(self, options):
        response = requests.get(f'{HOST_ASSETS}/project/registry/all')
        items = response.json()
        for slug in items:
            if self._exists(slug):
                print('Skipping: Asset with this alias ' + slug + ' already exists')
                continue
            data = items[slug]
            create_asset(data, asset_type='PROJECT')

    def quiz(self, options):
        response = requests.get(f'{HOST_ASSETS}/quiz/all')
        items = response.json()
        for quiz in items:
            slug = quiz['info']['slug']
            if self._exists(slug):
                print('Skipping: Asset with this alias ' + slug + ' already exists')
                continue
            data = {
                'slug': quiz['info']['slug'],
                'title': quiz['info']['name'],
                'status': quiz['info']['status'].upper() if 'status' in quiz['info'] else 'DRAFT',
                'description': quiz['info']['main'],
                'lang': quiz['info']['lang'],
                'config': quiz,
                'external': True,
                'interactive': True,
                'with_solutions': True,
                'graded': True,
            }
            create_asset(data, asset_type='QUIZ')