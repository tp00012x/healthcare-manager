import csv
import io

from account.models import Account
from django.contrib import messages
from django.shortcuts import render
from member.models import Member


def csv_upload(request):
    template = "profile_upload.html"

    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
        return render(request, template)

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    members = []
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        account = Account.objects.get_or_create(id=column[5])[0]
        members.append(Member(
            first_name=column[1],
            last_name=column[2],
            phone_number=f'+1{column[3]}',
            client_member_id=column[4],
            account_id=account,
        ))
    # Bulk create objects
    Member.objects.bulk_create(members, ignore_conflicts=True)
    return render(request, template)
