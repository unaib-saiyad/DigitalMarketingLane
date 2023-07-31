from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet

from .models import Invoice, InvoiceDetail
from .serializers import *


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class GetInvoiceModelViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerilizer
    allowed_methods = ('GET', 'POST')
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def list(self, request, *args, **kwargs):
        name = self.request.query_params.get('customer_name', None)
        if name:
            self.queryset = Invoice.objects.filter(customer_name=name)
        else:
            self.queryset = {}
        return super(GetInvoiceModelViewSet, self).list(request, *args, **kwargs)


class GetInvoiceDetailModelViewSet(ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerilizer
    allowed_methods = ('GET', 'POST')
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def list(self, request, *args, **kwargs):
        name = self.request.query_params.get('customer_name', None)
        if name:
            invoice = Invoice.objects.filter(customer_name=name).last()
            if not invoice:
                self.queryset = {}
            else:
                self.queryset = self.queryset.filter(invoice=invoice)
        else:
            self.queryset = {}
        return super(GetInvoiceDetailModelViewSet, self).list(request, *args, **kwargs)
