from django.core.management.base import BaseCommand, CommandError
from reparacao.models import Reparacao
from reparacao.calc_rules import *

class Command(BaseCommand):

    def add_arguments(self, parser):
        qs = Reparacao.objects.exclude(price='0.00').filter(total_to_pay='0.00')
        for q in qs.values():

            dict= {}
            dict = calc_total(q)
            q['total_to_pay']=dict['total_to_pay']
            q['total_to_pay_with_tax']=dict['total_to_pay_with_tax']
            q['tax_to_pay']=dict['tax_to_pay']
            a=Reparacao.objects.filter(id=q['id'])
            a.update(total_to_pay=q['total_to_pay'])
            a.update(total_to_pay_with_tax=q['total_to_pay_with_tax'])
            a.update(tax_to_pay=q['tax_to_pay'])
            parser.add_argument('qs', nargs='+', type=int)


    def handle(self, *args, **options):
        for id in options['qs']:
            try:
                pass
            except Reparacao.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % id)

            id.opened = False
            id.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % id))