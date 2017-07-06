# -*- coding: utf-8 -*-

"""
   telesignverifyapi.http.auth.custom_auth

   This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""

from ...configuration import Configuration

class CustomAuth:

    @staticmethod
    def apply(http_request):
        """ Add custom authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object with fields you can modify.

        """
        # TODO: Add your custom authentication here
        # The following properties are available to use
        #     Configuration.customer_id
        #     Configuration.api_key
        # 
        # Example: 
        # Add a header through: http_request.headers["key"] = "value"