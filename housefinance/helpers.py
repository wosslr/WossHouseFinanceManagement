from .models import AccountingDocumentHeader


class ChartSpendMonthlyHelper:
    @staticmethod
    def get_periods():
        result = {}
        acc_header_list = AccountingDocumentHeader.objects.all().values('creation_date').distinct()
        for acc_header in acc_header_list.iterator():
            acc_header_date = acc_header['creation_date']
            key = str(acc_header_date.year) + str(acc_header_date.month)
            result[key] = {'year': acc_header_date.year, 'month': acc_header_date.month}

        return result
