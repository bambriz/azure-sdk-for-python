# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class ManagedServiceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity (where both SystemAssigned and UserAssigned types are
    allowed).
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class MarketplaceSubscriptionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Marketplace subscription status of a resource."""

    PENDING_FULFILLMENT_START = "PendingFulfillmentStart"
    """Purchased but not yet activated"""
    SUBSCRIBED = "Subscribed"
    """Marketplace subscription is activated"""
    SUSPENDED = "Suspended"
    """This state indicates that a customer's payment for the Marketplace service was not received"""
    UNSUBSCRIBED = "Unsubscribed"
    """Customer has cancelled the subscription"""


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class ResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of a resource type."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""


class SingleSignOnStates(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Various states of the SSO resource."""

    INITIAL = "Initial"
    """Initial state of the SSO resource"""
    ENABLE = "Enable"
    """State of the SSO resource when it is enabled"""
    DISABLE = "Disable"
    """State of the SSO resource when it is disabled"""


class Versions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Supported API versions for the Astronomer.Astro resource provider."""

    V1_PREVIEW = "2023-08-01"
    """Dependent on Azure.ResourceManager.Versions.v1_0_Preview_1, LiftrBase.Versions.v1_preview,
    #: LiftrBase.Data.Versions.v1_preview"""
