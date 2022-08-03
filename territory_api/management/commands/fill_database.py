import csv
import os 

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from territory_api.models import Territory


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        csv_path = os.path.join(settings.BASE_DIR, "data_test_FS","territories.csv")
        try: 
            with open(csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    row['is_current'] = True if row['is_current'] == 'true' else False
                    row['population'] = None if row['population'] == '' else row['population']
                    t = Territory.objects.get_or_create(id=row['id'], code=row['code'], name=row['name'], kind=row['kind'],created_at=row['created_at'], updated_at=row['updated_at'], is_current=row['is_current'], population=row['population'], official_website_url=row['official_website_url'], articles_count=row['articles_count'], admin_docs_count=row['admin_docs_count'],impacters_count=row['impacters_count'], websites_count=row['websites_count'], sources_count=row['sources_count'])

            self.stdout.write(self.style.SUCCESS('Successfully filled the databse'))
        except Exception as e:
            raise CommandError(f'Error during the process: {e}')