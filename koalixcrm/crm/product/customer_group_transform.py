# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _


class CustomerGroupTransform(models.Model):
    from_customer_group = models.ForeignKey('CustomerGroup',
                                            verbose_name=_("From Unit"),
                                            related_name="db_reltransfromfromcustomergroup",
                                            blank=False,
                                            null=False)
    to_customer_group = models.ForeignKey('CustomerGroup',
                                          verbose_name=_("To Unit"),
                                          related_name="db_reltransfromtocustomergroup",
                                          blank=False,
                                          null=False)
    product = models.ForeignKey('Product',
                                verbose_name=_("Product"),
                                blank=False,
                                null=False)
    factor = models.IntegerField(verbose_name=_("Factor between From and To Customer Group"),
                                 blank=True,
                                 null=True)

    def transform(self, customer_group):
        """The transform function verifies whether the provided argument customer_group
        is corresponding with the "from_customer_group" variable of the CustomerGroupTransform class
        When this is ok, the function returns the "to_customer_group". When the provided customer_group
        argument is not corresponding, the function returns a "None"

        Args:
        customer_group: CustomerGroup object

        Returns:
        CustomerGroup object or None

        Raises:
        No exceptions planned"""
        if self.from_customer_group == customer_group:
            return self.to_customer_group
        else:
            return None

    def __str__(self):
        return "From " + self.from_customer_group.name + " to " + self.to_customer_group.name

    class Meta:
        app_label = "crm"
        verbose_name = _('Customer Group Price Transform')
        verbose_name_plural = _('Customer Group Price Transforms')