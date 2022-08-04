import csv
import os 

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from territory_api.models import Territory, Territory_Parents


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)
    
    def __fill_territory(self):
        try: 
            csv_path = os.path.join(settings.BASE_DIR, "data_test_FS","territories.csv")
            with open(csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    # Clean Data 
                    row['is_current'] = True if row['is_current'] == 'true' else False
                    row['population'] = None if row['population'] == '' else row['population']
                    # Insert Data
                    Territory.objects.get_or_create(id=row['id'], code=row['code'], name=row['name'], kind=row['kind'],created_at=row['created_at'], updated_at=row['updated_at'], is_current=row['is_current'], population=row['population'], official_website_url=row['official_website_url'], articles_count=row['articles_count'], admin_docs_count=row['admin_docs_count'],impacters_count=row['impacters_count'], websites_count=row['websites_count'], sources_count=row['sources_count'])
            self.stdout.write(self.style.SUCCESS('Successfully filled the database with territories data.'))
        except Exception as e:
            raise CommandError(f'Error during the process: {e}')
        
    def __fill_territory_parents(self):
        try: 
            csv_path = os.path.join(settings.BASE_DIR, "data_test_FS","territory_parents.csv")
            with open(csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    # Clean Data
                    row['child_id'] = Territory.objects.get(id=int(row['child_id']))
                    row['parent_id'] = Territory.objects.get(id=int(row['parent_id']))
                    # Insert Data
                    Territory_Parents.objects.get_or_create(id=row['id'], child_id=row['child_id'], parent_id=row['parent_id'], created_at=row['created_at'], updated_at=row['updated_at'])
            self.stdout.write(self.style.SUCCESS('Successfully filled the database with territories relationships data.'))
        except Exception as e:
            raise CommandError(f'Error during the process: {e}')

    def handle(self, *args, **options):
        self.__fill_territory()
        self.__fill_territory_parents()
        