from rest_framework import serializers
from .models import Invoice, InvoiceDetail


class InvoiceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceDetailSerilizer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField('get_customer_name')
    date = serializers.SerializerMethodField('get_date')

    class Meta:
        model = InvoiceDetail
        fields = '__all__'

    def get_customer_name(self, obj):
        return obj.invoice.customer_name

    def get_date(self, obj):
        return obj.invoice.date
