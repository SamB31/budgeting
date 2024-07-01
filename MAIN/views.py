from django.shortcuts import render, get_object_or_404, redirect
from .models import Bucket, Transaction
from django.core.paginator import Paginator
from .forms import TransactionFilterForm
from django.views.decorators.http import require_POST


def bucket_overview(request):
    buckets = Bucket.objects.all()
    return render(request, 'bucket_overview.html', {'buckets': buckets})

def transaction_list(request):
    transactions = Transaction.objects.all()
    paginator = Paginator(transactions, 10)  # Show 10 transactions per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    filter_form = TransactionFilterForm(request.GET or None)

    if filter_form.is_valid():
        if filter_form.cleaned_data['start_date']:
            page_obj = page_obj.filter(date__gte=filter_form.cleaned_data['start_date'])
        if filter_form.cleaned_data['end_date']:
            page_obj = page_obj.filter(date__lte=filter_form.cleaned_data['end_date'])
        if filter_form.cleaned_data['search']:
            page_obj = page_obj.filter(description__icontains=filter_form.cleaned_data['search'])

    buckets = Bucket.objects.all()
    return render(request, 'transaction_list.html', {'page_obj': page_obj, 'buckets': buckets, 'filter_form': filter_form})

def assign_bucket(request, transaction_id, bucket_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if bucket_id == 0:
        transaction.bucket = None
    else:
        bucket = get_object_or_404(Bucket, id=bucket_id)
        transaction.bucket = bucket
    transaction.save()
    return redirect('transaction_list')

@require_POST
def assign_simple_description(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    simple_description = request.POST.get('simple_description', '').strip()
    if simple_description:
        transaction.simple_description = simple_description
        transaction.save()
    return redirect('transaction_list')

