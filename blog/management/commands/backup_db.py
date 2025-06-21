import os
import gzip
import json
from datetime import datetime
from pathlib import Path

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from django.core.serializers import serialize
from blog.models import Post, Category


class Command(BaseCommand):
    help = 'Create a backup of the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--compress',
            action='store_true',
            help='Compress the backup file with gzip',
        )
        parser.add_argument(
            '--output-dir',
            type=str,
            default='backups',
            help='Directory to store backup files (default: backups)',
        )

    def handle(self, *args, **options):
        # Create backup directory if it doesn't exist
        backup_dir = Path(options['output_dir'])
        backup_dir.mkdir(exist_ok=True)
        
        # Generate timestamp for filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Create backup filename
        backup_filename = f'blog_backup_{timestamp}.json'
        if options['compress']:
            backup_filename += '.gz'
        
        backup_path = backup_dir / backup_filename
        
        self.stdout.write(f'Creating backup: {backup_path}')
        
        try:
            # Create backup data using Django's serialization
            backup_data = {
                'timestamp': datetime.now().isoformat(),
                'django_version': getattr(settings, 'DJANGO_VERSION', 'unknown'),
                'database_engine': settings.DATABASES['default']['ENGINE'],
                'data': {}
            }
            
            # Backup all app data using dumpdata
            apps_to_backup = ['blog', 'auth', 'contenttypes']
            
            for app in apps_to_backup:
                self.stdout.write(f'Backing up {app}...')
                # Use call_command to get dumpdata output
                from io import StringIO
                output = StringIO()
                call_command('dumpdata', app, stdout=output, indent=2)
                backup_data['data'][app] = json.loads(output.getvalue())
            
            # Write backup file
            if options['compress']:
                with gzip.open(backup_path, 'wt', encoding='utf-8') as f:
                    json.dump(backup_data, f, indent=2, ensure_ascii=False)
            else:
                with open(backup_path, 'w', encoding='utf-8') as f:
                    json.dump(backup_data, f, indent=2, ensure_ascii=False)
            
            # Get file size for reporting
            file_size = backup_path.stat().st_size
            size_mb = file_size / (1024 * 1024)
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Backup created successfully: {backup_path}'
                )
            )
            self.stdout.write(f'File size: {size_mb:.2f} MB')
            self.stdout.write(f'Records backed up:')
            
            # Report what was backed up
            for app, data in backup_data['data'].items():
                self.stdout.write(f'  {app}: {len(data)} records')
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Backup failed: {str(e)}')
            )
            raise