# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE.txt in the project root for
# license information.
# -------------------------------------------------------------------------
import pytest

from azure.core.exceptions import ResourceNotFoundError, HttpResponseError
from azure.digitaltwins.core import DigitalTwinsClient, DigitalTwinsEventRoute
from devtools_testutils import AzureRecordedTestCase


class TestDigitalTwinsEventRoute(AzureRecordedTestCase):

    def _get_client(self, endpoint, **kwargs):
        credential = self.get_credential(DigitalTwinsClient)
        return self.create_client_from_credential(
            DigitalTwinsClient,
            credential,
            endpoint=endpoint,
            **kwargs)

    def test_create_event_route_no_endpoint(self, recorded_test, digitaltwin):
        event_route_id = self.create_random_name('eventRoute-')
        event_filter = "$eventType = 'DigitalTwinTelemetryMessages' or $eventType = 'DigitalTwinLifecycleNotification'"
        endpoint = self.create_random_name('endpoint-')
        route = DigitalTwinsEventRoute(
            endpoint_name=endpoint,
            filter=event_filter
        )
        client = self._get_client(digitaltwin["endpoint"])
        with pytest.raises(HttpResponseError):
            client.upsert_event_route(event_route_id, route)

    def test_get_event_route_not_existing(self, recorded_test, digitaltwin):
        event_route_id = self.create_random_name('eventRoute-')
        client = self._get_client(digitaltwin["endpoint"])
        with pytest.raises(ResourceNotFoundError):
            client.get_event_route(event_route_id)

    def test_list_event_routes(self, recorded_test, digitaltwin):
        client = self._get_client(digitaltwin["endpoint"])
        all_routes = list(client.list_event_routes())
        assert all_routes == []

    def test_delete_event_route_not_existing(self, recorded_test, digitaltwin):
        event_route_id = self.create_random_name('eventRoute-')
        client = self._get_client(digitaltwin["endpoint"])
        with pytest.raises(ResourceNotFoundError):
            client.delete_event_route(event_route_id)
