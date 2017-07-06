# -*- coding: utf-8 -*-

"""
   telesignverifyapi.configuration

   This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from .api_helper import APIHelper

class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "indexed"

    # The base Uri for API calls
    base_uri = 'https://rest-ww.telesign.com/v1'

    # TODO: Set an appropriate value
    customer_id = "TODO: Replace"

    # TODO: Set an appropriate value
    api_key = "TODO: Replace"
