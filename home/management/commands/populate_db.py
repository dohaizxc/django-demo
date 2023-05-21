from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random
from datetime import datetime, timedelta
from pytz import utc
from home.models import Topic, Course

class Command(BaseCommand):
    help = "Populates the database with randomly generated data."

    def add_arguments(self, parser):
        parser.add_argument("--amount", type=int, help="The number of courses to create.")

    def handle(self, *args, **options):
        fake = Faker()
        topics = Topic.objects.all()
        amount = options["amount"] if options["amount"] else 2500
        for _ in range(amount):
            dt = timezone.now() - timedelta(days=random.randint(0, 1825))
            topic = random.choice(topics)
            course = Course.objects.create(
                name=fake.word(),
                description=fake.paragraph(),
                topic=topic,
                type=random.choice(Course.TYPE)[0],
                create=dt,
                updated=dt,
            )
            course.save()

        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))
