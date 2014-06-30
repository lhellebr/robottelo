# -*- encoding: utf-8 -*-

"""
Module for Medium api an record implementation
"""


from robottelo.common import records
from robottelo.api.apicrud import ApiCrud
from robottelo.records.operatingsystem import OperatingSystem


class MediumApi(ApiCrud):
    """ Implementation of api for  foreman media
    """
    api_path = "/api/media/"
    api_json_key = u"medium"
    create_fields = ["name",
                     "path",
                     "operatingsystem_ids"]


class Medium(records.Record):
    """ Implementation of foreman media record
    Utilizes _post_init to ensure, that name matches domain,
    operating system matches architecture and partition table
    """
    name = records.BasicPositiveField()
    path = records.StringField("http://mirror.centos.org/centos/6.5/os/x86_64/") # TODO
    operatingsystem = records.ManyRelatedField(OperatingSystem, 1, 3)

    def _post_init(self):
        """Ensures, that certain fields are consistent
        with api requirements
        """
        pass

    class Meta:
        """Linking record definition with api implementation.
        """
        api_class = MediumApi
