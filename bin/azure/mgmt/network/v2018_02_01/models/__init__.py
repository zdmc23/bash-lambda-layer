# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AddressSpace
    from ._models_py3 import ApplicationGateway
    from ._models_py3 import ApplicationGatewayAuthenticationCertificate
    from ._models_py3 import ApplicationGatewayAvailableSslOptions
    from ._models_py3 import ApplicationGatewayAvailableWafRuleSetsResult
    from ._models_py3 import ApplicationGatewayBackendAddress
    from ._models_py3 import ApplicationGatewayBackendAddressPool
    from ._models_py3 import ApplicationGatewayBackendHealth
    from ._models_py3 import ApplicationGatewayBackendHealthHttpSettings
    from ._models_py3 import ApplicationGatewayBackendHealthPool
    from ._models_py3 import ApplicationGatewayBackendHealthServer
    from ._models_py3 import ApplicationGatewayBackendHttpSettings
    from ._models_py3 import ApplicationGatewayConnectionDraining
    from ._models_py3 import ApplicationGatewayFirewallDisabledRuleGroup
    from ._models_py3 import ApplicationGatewayFirewallRule
    from ._models_py3 import ApplicationGatewayFirewallRuleGroup
    from ._models_py3 import ApplicationGatewayFirewallRuleSet
    from ._models_py3 import ApplicationGatewayFrontendIPConfiguration
    from ._models_py3 import ApplicationGatewayFrontendPort
    from ._models_py3 import ApplicationGatewayHttpListener
    from ._models_py3 import ApplicationGatewayIPConfiguration
    from ._models_py3 import ApplicationGatewayPathRule
    from ._models_py3 import ApplicationGatewayProbe
    from ._models_py3 import ApplicationGatewayProbeHealthResponseMatch
    from ._models_py3 import ApplicationGatewayRedirectConfiguration
    from ._models_py3 import ApplicationGatewayRequestRoutingRule
    from ._models_py3 import ApplicationGatewaySku
    from ._models_py3 import ApplicationGatewaySslCertificate
    from ._models_py3 import ApplicationGatewaySslPolicy
    from ._models_py3 import ApplicationGatewaySslPredefinedPolicy
    from ._models_py3 import ApplicationGatewayUrlPathMap
    from ._models_py3 import ApplicationGatewayWebApplicationFirewallConfiguration
    from ._models_py3 import ApplicationSecurityGroup
    from ._models_py3 import Availability
    from ._models_py3 import AvailableProvidersList
    from ._models_py3 import AvailableProvidersListCity
    from ._models_py3 import AvailableProvidersListCountry
    from ._models_py3 import AvailableProvidersListParameters
    from ._models_py3 import AvailableProvidersListState
    from ._models_py3 import AzureAsyncOperationResult
    from ._models_py3 import AzureReachabilityReport
    from ._models_py3 import AzureReachabilityReportItem
    from ._models_py3 import AzureReachabilityReportLatencyInfo
    from ._models_py3 import AzureReachabilityReportLocation
    from ._models_py3 import AzureReachabilityReportParameters
    from ._models_py3 import BackendAddressPool
    from ._models_py3 import BGPCommunity
    from ._models_py3 import BgpPeerStatus
    from ._models_py3 import BgpPeerStatusListResult
    from ._models_py3 import BgpServiceCommunity
    from ._models_py3 import BgpSettings
    from ._models_py3 import ConnectionMonitor
    from ._models_py3 import ConnectionMonitorDestination
    from ._models_py3 import ConnectionMonitorParameters
    from ._models_py3 import ConnectionMonitorQueryResult
    from ._models_py3 import ConnectionMonitorResult
    from ._models_py3 import ConnectionMonitorSource
    from ._models_py3 import ConnectionResetSharedKey
    from ._models_py3 import ConnectionSharedKey
    from ._models_py3 import ConnectionStateSnapshot
    from ._models_py3 import ConnectivityDestination
    from ._models_py3 import ConnectivityHop
    from ._models_py3 import ConnectivityInformation
    from ._models_py3 import ConnectivityIssue
    from ._models_py3 import ConnectivityParameters
    from ._models_py3 import ConnectivitySource
    from ._models_py3 import DdosProtectionPlan
    from ._models_py3 import DhcpOptions
    from ._models_py3 import Dimension
    from ._models_py3 import DnsNameAvailabilityResult
    from ._models_py3 import EffectiveNetworkSecurityGroup
    from ._models_py3 import EffectiveNetworkSecurityGroupAssociation
    from ._models_py3 import EffectiveNetworkSecurityGroupListResult
    from ._models_py3 import EffectiveNetworkSecurityRule
    from ._models_py3 import EffectiveRoute
    from ._models_py3 import EffectiveRouteListResult
    from ._models_py3 import EndpointServiceResult
    from ._models_py3 import Error
    from ._models_py3 import ErrorDetails
    from ._models_py3 import ExpressRouteCircuit
    from ._models_py3 import ExpressRouteCircuitArpTable
    from ._models_py3 import ExpressRouteCircuitAuthorization
    from ._models_py3 import ExpressRouteCircuitConnection
    from ._models_py3 import ExpressRouteCircuitPeering
    from ._models_py3 import ExpressRouteCircuitPeeringConfig
    from ._models_py3 import ExpressRouteCircuitReference
    from ._models_py3 import ExpressRouteCircuitRoutesTable
    from ._models_py3 import ExpressRouteCircuitRoutesTableSummary
    from ._models_py3 import ExpressRouteCircuitsArpTableListResult
    from ._models_py3 import ExpressRouteCircuitServiceProviderProperties
    from ._models_py3 import ExpressRouteCircuitSku
    from ._models_py3 import ExpressRouteCircuitsRoutesTableListResult
    from ._models_py3 import ExpressRouteCircuitsRoutesTableSummaryListResult
    from ._models_py3 import ExpressRouteCircuitStats
    from ._models_py3 import ExpressRouteCrossConnection
    from ._models_py3 import ExpressRouteCrossConnectionPeering
    from ._models_py3 import ExpressRouteCrossConnectionRoutesTableSummary
    from ._models_py3 import ExpressRouteCrossConnectionsRoutesTableSummaryListResult
    from ._models_py3 import ExpressRouteServiceProvider
    from ._models_py3 import ExpressRouteServiceProviderBandwidthsOffered
    from ._models_py3 import FlowLogInformation
    from ._models_py3 import FlowLogStatusParameters
    from ._models_py3 import FrontendIPConfiguration
    from ._models_py3 import GatewayRoute
    from ._models_py3 import GatewayRouteListResult
    from ._models_py3 import HTTPConfiguration
    from ._models_py3 import HTTPHeader
    from ._models_py3 import InboundNatPool
    from ._models_py3 import InboundNatRule
    from ._models_py3 import IPAddressAvailabilityResult
    from ._models_py3 import IPConfiguration
    from ._models_py3 import IpsecPolicy
    from ._models_py3 import IpTag
    from ._models_py3 import Ipv6ExpressRouteCircuitPeeringConfig
    from ._models_py3 import LoadBalancer
    from ._models_py3 import LoadBalancerSku
    from ._models_py3 import LoadBalancingRule
    from ._models_py3 import LocalNetworkGateway
    from ._models_py3 import LogSpecification
    from ._models_py3 import MetricSpecification
    from ._models_py3 import NetworkInterface
    from ._models_py3 import NetworkInterfaceAssociation
    from ._models_py3 import NetworkInterfaceDnsSettings
    from ._models_py3 import NetworkInterfaceIPConfiguration
    from ._models_py3 import NetworkSecurityGroup
    from ._models_py3 import NetworkWatcher
    from ._models_py3 import NextHopParameters
    from ._models_py3 import NextHopResult
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationPropertiesFormatServiceSpecification
    from ._models_py3 import OutboundNatRule
    from ._models_py3 import PacketCapture
    from ._models_py3 import PacketCaptureFilter
    from ._models_py3 import PacketCaptureParameters
    from ._models_py3 import PacketCaptureQueryStatusResult
    from ._models_py3 import PacketCaptureResult
    from ._models_py3 import PacketCaptureStorageLocation
    from ._models_py3 import PatchRouteFilter
    from ._models_py3 import PatchRouteFilterRule
    from ._models_py3 import Probe
    from ._models_py3 import ProtocolConfiguration
    from ._models_py3 import PublicIPAddress
    from ._models_py3 import PublicIPAddressDnsSettings
    from ._models_py3 import PublicIPAddressSku
    from ._models_py3 import QueryTroubleshootingParameters
    from ._models_py3 import Resource
    from ._models_py3 import ResourceNavigationLink
    from ._models_py3 import RetentionPolicyParameters
    from ._models_py3 import Route
    from ._models_py3 import RouteFilter
    from ._models_py3 import RouteFilterRule
    from ._models_py3 import RouteTable
    from ._models_py3 import SecurityGroupNetworkInterface
    from ._models_py3 import SecurityGroupViewParameters
    from ._models_py3 import SecurityGroupViewResult
    from ._models_py3 import SecurityRule
    from ._models_py3 import SecurityRuleAssociations
    from ._models_py3 import ServiceEndpointPropertiesFormat
    from ._models_py3 import Subnet
    from ._models_py3 import SubnetAssociation
    from ._models_py3 import SubResource
    from ._models_py3 import TagsObject
    from ._models_py3 import Topology
    from ._models_py3 import TopologyAssociation
    from ._models_py3 import TopologyParameters
    from ._models_py3 import TopologyResource
    from ._models_py3 import TroubleshootingDetails
    from ._models_py3 import TroubleshootingParameters
    from ._models_py3 import TroubleshootingRecommendedActions
    from ._models_py3 import TroubleshootingResult
    from ._models_py3 import TunnelConnectionHealth
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import VerificationIPFlowParameters
    from ._models_py3 import VerificationIPFlowResult
    from ._models_py3 import VirtualNetwork
    from ._models_py3 import VirtualNetworkConnectionGatewayReference
    from ._models_py3 import VirtualNetworkGateway
    from ._models_py3 import VirtualNetworkGatewayConnection
    from ._models_py3 import VirtualNetworkGatewayConnectionListEntity
    from ._models_py3 import VirtualNetworkGatewayIPConfiguration
    from ._models_py3 import VirtualNetworkGatewaySku
    from ._models_py3 import VirtualNetworkPeering
    from ._models_py3 import VirtualNetworkUsage
    from ._models_py3 import VirtualNetworkUsageName
    from ._models_py3 import VpnClientConfiguration
    from ._models_py3 import VpnClientIPsecParameters
    from ._models_py3 import VpnClientParameters
    from ._models_py3 import VpnClientRevokedCertificate
    from ._models_py3 import VpnClientRootCertificate
    from ._models_py3 import VpnDeviceScriptParameters
except (SyntaxError, ImportError):
    from ._models import AddressSpace
    from ._models import ApplicationGateway
    from ._models import ApplicationGatewayAuthenticationCertificate
    from ._models import ApplicationGatewayAvailableSslOptions
    from ._models import ApplicationGatewayAvailableWafRuleSetsResult
    from ._models import ApplicationGatewayBackendAddress
    from ._models import ApplicationGatewayBackendAddressPool
    from ._models import ApplicationGatewayBackendHealth
    from ._models import ApplicationGatewayBackendHealthHttpSettings
    from ._models import ApplicationGatewayBackendHealthPool
    from ._models import ApplicationGatewayBackendHealthServer
    from ._models import ApplicationGatewayBackendHttpSettings
    from ._models import ApplicationGatewayConnectionDraining
    from ._models import ApplicationGatewayFirewallDisabledRuleGroup
    from ._models import ApplicationGatewayFirewallRule
    from ._models import ApplicationGatewayFirewallRuleGroup
    from ._models import ApplicationGatewayFirewallRuleSet
    from ._models import ApplicationGatewayFrontendIPConfiguration
    from ._models import ApplicationGatewayFrontendPort
    from ._models import ApplicationGatewayHttpListener
    from ._models import ApplicationGatewayIPConfiguration
    from ._models import ApplicationGatewayPathRule
    from ._models import ApplicationGatewayProbe
    from ._models import ApplicationGatewayProbeHealthResponseMatch
    from ._models import ApplicationGatewayRedirectConfiguration
    from ._models import ApplicationGatewayRequestRoutingRule
    from ._models import ApplicationGatewaySku
    from ._models import ApplicationGatewaySslCertificate
    from ._models import ApplicationGatewaySslPolicy
    from ._models import ApplicationGatewaySslPredefinedPolicy
    from ._models import ApplicationGatewayUrlPathMap
    from ._models import ApplicationGatewayWebApplicationFirewallConfiguration
    from ._models import ApplicationSecurityGroup
    from ._models import Availability
    from ._models import AvailableProvidersList
    from ._models import AvailableProvidersListCity
    from ._models import AvailableProvidersListCountry
    from ._models import AvailableProvidersListParameters
    from ._models import AvailableProvidersListState
    from ._models import AzureAsyncOperationResult
    from ._models import AzureReachabilityReport
    from ._models import AzureReachabilityReportItem
    from ._models import AzureReachabilityReportLatencyInfo
    from ._models import AzureReachabilityReportLocation
    from ._models import AzureReachabilityReportParameters
    from ._models import BackendAddressPool
    from ._models import BGPCommunity
    from ._models import BgpPeerStatus
    from ._models import BgpPeerStatusListResult
    from ._models import BgpServiceCommunity
    from ._models import BgpSettings
    from ._models import ConnectionMonitor
    from ._models import ConnectionMonitorDestination
    from ._models import ConnectionMonitorParameters
    from ._models import ConnectionMonitorQueryResult
    from ._models import ConnectionMonitorResult
    from ._models import ConnectionMonitorSource
    from ._models import ConnectionResetSharedKey
    from ._models import ConnectionSharedKey
    from ._models import ConnectionStateSnapshot
    from ._models import ConnectivityDestination
    from ._models import ConnectivityHop
    from ._models import ConnectivityInformation
    from ._models import ConnectivityIssue
    from ._models import ConnectivityParameters
    from ._models import ConnectivitySource
    from ._models import DdosProtectionPlan
    from ._models import DhcpOptions
    from ._models import Dimension
    from ._models import DnsNameAvailabilityResult
    from ._models import EffectiveNetworkSecurityGroup
    from ._models import EffectiveNetworkSecurityGroupAssociation
    from ._models import EffectiveNetworkSecurityGroupListResult
    from ._models import EffectiveNetworkSecurityRule
    from ._models import EffectiveRoute
    from ._models import EffectiveRouteListResult
    from ._models import EndpointServiceResult
    from ._models import Error
    from ._models import ErrorDetails
    from ._models import ExpressRouteCircuit
    from ._models import ExpressRouteCircuitArpTable
    from ._models import ExpressRouteCircuitAuthorization
    from ._models import ExpressRouteCircuitConnection
    from ._models import ExpressRouteCircuitPeering
    from ._models import ExpressRouteCircuitPeeringConfig
    from ._models import ExpressRouteCircuitReference
    from ._models import ExpressRouteCircuitRoutesTable
    from ._models import ExpressRouteCircuitRoutesTableSummary
    from ._models import ExpressRouteCircuitsArpTableListResult
    from ._models import ExpressRouteCircuitServiceProviderProperties
    from ._models import ExpressRouteCircuitSku
    from ._models import ExpressRouteCircuitsRoutesTableListResult
    from ._models import ExpressRouteCircuitsRoutesTableSummaryListResult
    from ._models import ExpressRouteCircuitStats
    from ._models import ExpressRouteCrossConnection
    from ._models import ExpressRouteCrossConnectionPeering
    from ._models import ExpressRouteCrossConnectionRoutesTableSummary
    from ._models import ExpressRouteCrossConnectionsRoutesTableSummaryListResult
    from ._models import ExpressRouteServiceProvider
    from ._models import ExpressRouteServiceProviderBandwidthsOffered
    from ._models import FlowLogInformation
    from ._models import FlowLogStatusParameters
    from ._models import FrontendIPConfiguration
    from ._models import GatewayRoute
    from ._models import GatewayRouteListResult
    from ._models import HTTPConfiguration
    from ._models import HTTPHeader
    from ._models import InboundNatPool
    from ._models import InboundNatRule
    from ._models import IPAddressAvailabilityResult
    from ._models import IPConfiguration
    from ._models import IpsecPolicy
    from ._models import IpTag
    from ._models import Ipv6ExpressRouteCircuitPeeringConfig
    from ._models import LoadBalancer
    from ._models import LoadBalancerSku
    from ._models import LoadBalancingRule
    from ._models import LocalNetworkGateway
    from ._models import LogSpecification
    from ._models import MetricSpecification
    from ._models import NetworkInterface
    from ._models import NetworkInterfaceAssociation
    from ._models import NetworkInterfaceDnsSettings
    from ._models import NetworkInterfaceIPConfiguration
    from ._models import NetworkSecurityGroup
    from ._models import NetworkWatcher
    from ._models import NextHopParameters
    from ._models import NextHopResult
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import OperationPropertiesFormatServiceSpecification
    from ._models import OutboundNatRule
    from ._models import PacketCapture
    from ._models import PacketCaptureFilter
    from ._models import PacketCaptureParameters
    from ._models import PacketCaptureQueryStatusResult
    from ._models import PacketCaptureResult
    from ._models import PacketCaptureStorageLocation
    from ._models import PatchRouteFilter
    from ._models import PatchRouteFilterRule
    from ._models import Probe
    from ._models import ProtocolConfiguration
    from ._models import PublicIPAddress
    from ._models import PublicIPAddressDnsSettings
    from ._models import PublicIPAddressSku
    from ._models import QueryTroubleshootingParameters
    from ._models import Resource
    from ._models import ResourceNavigationLink
    from ._models import RetentionPolicyParameters
    from ._models import Route
    from ._models import RouteFilter
    from ._models import RouteFilterRule
    from ._models import RouteTable
    from ._models import SecurityGroupNetworkInterface
    from ._models import SecurityGroupViewParameters
    from ._models import SecurityGroupViewResult
    from ._models import SecurityRule
    from ._models import SecurityRuleAssociations
    from ._models import ServiceEndpointPropertiesFormat
    from ._models import Subnet
    from ._models import SubnetAssociation
    from ._models import SubResource
    from ._models import TagsObject
    from ._models import Topology
    from ._models import TopologyAssociation
    from ._models import TopologyParameters
    from ._models import TopologyResource
    from ._models import TroubleshootingDetails
    from ._models import TroubleshootingParameters
    from ._models import TroubleshootingRecommendedActions
    from ._models import TroubleshootingResult
    from ._models import TunnelConnectionHealth
    from ._models import Usage
    from ._models import UsageName
    from ._models import VerificationIPFlowParameters
    from ._models import VerificationIPFlowResult
    from ._models import VirtualNetwork
    from ._models import VirtualNetworkConnectionGatewayReference
    from ._models import VirtualNetworkGateway
    from ._models import VirtualNetworkGatewayConnection
    from ._models import VirtualNetworkGatewayConnectionListEntity
    from ._models import VirtualNetworkGatewayIPConfiguration
    from ._models import VirtualNetworkGatewaySku
    from ._models import VirtualNetworkPeering
    from ._models import VirtualNetworkUsage
    from ._models import VirtualNetworkUsageName
    from ._models import VpnClientConfiguration
    from ._models import VpnClientIPsecParameters
    from ._models import VpnClientParameters
    from ._models import VpnClientRevokedCertificate
    from ._models import VpnClientRootCertificate
    from ._models import VpnDeviceScriptParameters
from ._paged_models import ApplicationGatewayPaged
from ._paged_models import ApplicationGatewaySslPredefinedPolicyPaged
from ._paged_models import ApplicationSecurityGroupPaged
from ._paged_models import BackendAddressPoolPaged
from ._paged_models import BgpServiceCommunityPaged
from ._paged_models import ConnectionMonitorResultPaged
from ._paged_models import DdosProtectionPlanPaged
from ._paged_models import EndpointServiceResultPaged
from ._paged_models import ExpressRouteCircuitAuthorizationPaged
from ._paged_models import ExpressRouteCircuitPaged
from ._paged_models import ExpressRouteCircuitPeeringPaged
from ._paged_models import ExpressRouteCrossConnectionPaged
from ._paged_models import ExpressRouteCrossConnectionPeeringPaged
from ._paged_models import ExpressRouteServiceProviderPaged
from ._paged_models import FrontendIPConfigurationPaged
from ._paged_models import InboundNatRulePaged
from ._paged_models import LoadBalancerPaged
from ._paged_models import LoadBalancingRulePaged
from ._paged_models import LocalNetworkGatewayPaged
from ._paged_models import NetworkInterfaceIPConfigurationPaged
from ._paged_models import NetworkInterfacePaged
from ._paged_models import NetworkSecurityGroupPaged
from ._paged_models import NetworkWatcherPaged
from ._paged_models import OperationPaged
from ._paged_models import PacketCaptureResultPaged
from ._paged_models import ProbePaged
from ._paged_models import PublicIPAddressPaged
from ._paged_models import RouteFilterPaged
from ._paged_models import RouteFilterRulePaged
from ._paged_models import RoutePaged
from ._paged_models import RouteTablePaged
from ._paged_models import SecurityRulePaged
from ._paged_models import SubnetPaged
from ._paged_models import UsagePaged
from ._paged_models import VirtualNetworkGatewayConnectionListEntityPaged
from ._paged_models import VirtualNetworkGatewayConnectionPaged
from ._paged_models import VirtualNetworkGatewayPaged
from ._paged_models import VirtualNetworkPaged
from ._paged_models import VirtualNetworkPeeringPaged
from ._paged_models import VirtualNetworkUsagePaged
from ._network_management_client_enums import (
    TransportProtocol,
    IPAllocationMethod,
    IPVersion,
    SecurityRuleProtocol,
    SecurityRuleAccess,
    SecurityRuleDirection,
    RouteNextHopType,
    PublicIPAddressSkuName,
    ApplicationGatewayProtocol,
    ApplicationGatewayCookieBasedAffinity,
    ApplicationGatewayBackendHealthServerHealth,
    ApplicationGatewaySkuName,
    ApplicationGatewayTier,
    ApplicationGatewaySslProtocol,
    ApplicationGatewaySslPolicyType,
    ApplicationGatewaySslPolicyName,
    ApplicationGatewaySslCipherSuite,
    ApplicationGatewayRequestRoutingRuleType,
    ApplicationGatewayRedirectType,
    ApplicationGatewayOperationalState,
    ApplicationGatewayFirewallMode,
    AuthorizationUseStatus,
    ExpressRouteCircuitPeeringAdvertisedPublicPrefixState,
    Access,
    ExpressRoutePeeringType,
    ExpressRoutePeeringState,
    CircuitConnectionStatus,
    ExpressRouteCircuitPeeringState,
    ExpressRouteCircuitSkuTier,
    ExpressRouteCircuitSkuFamily,
    ServiceProviderProvisioningState,
    LoadBalancerSkuName,
    LoadDistribution,
    ProbeProtocol,
    NetworkOperationStatus,
    EffectiveSecurityRuleProtocol,
    EffectiveRouteSource,
    EffectiveRouteState,
    ProvisioningState,
    AssociationType,
    Direction,
    IpFlowProtocol,
    NextHopType,
    PcProtocol,
    PcStatus,
    PcError,
    Protocol,
    HTTPMethod,
    Origin,
    Severity,
    IssueType,
    ConnectionStatus,
    ConnectionMonitorSourceStatus,
    ConnectionState,
    EvaluationState,
    VirtualNetworkPeeringState,
    VirtualNetworkGatewayType,
    VpnType,
    VirtualNetworkGatewaySkuName,
    VirtualNetworkGatewaySkuTier,
    VpnClientProtocol,
    IpsecEncryption,
    IpsecIntegrity,
    IkeEncryption,
    IkeIntegrity,
    DhGroup,
    PfsGroup,
    BgpPeerState,
    ProcessorArchitecture,
    AuthenticationMethod,
    VirtualNetworkGatewayConnectionStatus,
    VirtualNetworkGatewayConnectionType,
)

__all__ = [
    'AddressSpace',
    'ApplicationGateway',
    'ApplicationGatewayAuthenticationCertificate',
    'ApplicationGatewayAvailableSslOptions',
    'ApplicationGatewayAvailableWafRuleSetsResult',
    'ApplicationGatewayBackendAddress',
    'ApplicationGatewayBackendAddressPool',
    'ApplicationGatewayBackendHealth',
    'ApplicationGatewayBackendHealthHttpSettings',
    'ApplicationGatewayBackendHealthPool',
    'ApplicationGatewayBackendHealthServer',
    'ApplicationGatewayBackendHttpSettings',
    'ApplicationGatewayConnectionDraining',
    'ApplicationGatewayFirewallDisabledRuleGroup',
    'ApplicationGatewayFirewallRule',
    'ApplicationGatewayFirewallRuleGroup',
    'ApplicationGatewayFirewallRuleSet',
    'ApplicationGatewayFrontendIPConfiguration',
    'ApplicationGatewayFrontendPort',
    'ApplicationGatewayHttpListener',
    'ApplicationGatewayIPConfiguration',
    'ApplicationGatewayPathRule',
    'ApplicationGatewayProbe',
    'ApplicationGatewayProbeHealthResponseMatch',
    'ApplicationGatewayRedirectConfiguration',
    'ApplicationGatewayRequestRoutingRule',
    'ApplicationGatewaySku',
    'ApplicationGatewaySslCertificate',
    'ApplicationGatewaySslPolicy',
    'ApplicationGatewaySslPredefinedPolicy',
    'ApplicationGatewayUrlPathMap',
    'ApplicationGatewayWebApplicationFirewallConfiguration',
    'ApplicationSecurityGroup',
    'Availability',
    'AvailableProvidersList',
    'AvailableProvidersListCity',
    'AvailableProvidersListCountry',
    'AvailableProvidersListParameters',
    'AvailableProvidersListState',
    'AzureAsyncOperationResult',
    'AzureReachabilityReport',
    'AzureReachabilityReportItem',
    'AzureReachabilityReportLatencyInfo',
    'AzureReachabilityReportLocation',
    'AzureReachabilityReportParameters',
    'BackendAddressPool',
    'BGPCommunity',
    'BgpPeerStatus',
    'BgpPeerStatusListResult',
    'BgpServiceCommunity',
    'BgpSettings',
    'ConnectionMonitor',
    'ConnectionMonitorDestination',
    'ConnectionMonitorParameters',
    'ConnectionMonitorQueryResult',
    'ConnectionMonitorResult',
    'ConnectionMonitorSource',
    'ConnectionResetSharedKey',
    'ConnectionSharedKey',
    'ConnectionStateSnapshot',
    'ConnectivityDestination',
    'ConnectivityHop',
    'ConnectivityInformation',
    'ConnectivityIssue',
    'ConnectivityParameters',
    'ConnectivitySource',
    'DdosProtectionPlan',
    'DhcpOptions',
    'Dimension',
    'DnsNameAvailabilityResult',
    'EffectiveNetworkSecurityGroup',
    'EffectiveNetworkSecurityGroupAssociation',
    'EffectiveNetworkSecurityGroupListResult',
    'EffectiveNetworkSecurityRule',
    'EffectiveRoute',
    'EffectiveRouteListResult',
    'EndpointServiceResult',
    'Error',
    'ErrorDetails',
    'ExpressRouteCircuit',
    'ExpressRouteCircuitArpTable',
    'ExpressRouteCircuitAuthorization',
    'ExpressRouteCircuitConnection',
    'ExpressRouteCircuitPeering',
    'ExpressRouteCircuitPeeringConfig',
    'ExpressRouteCircuitReference',
    'ExpressRouteCircuitRoutesTable',
    'ExpressRouteCircuitRoutesTableSummary',
    'ExpressRouteCircuitsArpTableListResult',
    'ExpressRouteCircuitServiceProviderProperties',
    'ExpressRouteCircuitSku',
    'ExpressRouteCircuitsRoutesTableListResult',
    'ExpressRouteCircuitsRoutesTableSummaryListResult',
    'ExpressRouteCircuitStats',
    'ExpressRouteCrossConnection',
    'ExpressRouteCrossConnectionPeering',
    'ExpressRouteCrossConnectionRoutesTableSummary',
    'ExpressRouteCrossConnectionsRoutesTableSummaryListResult',
    'ExpressRouteServiceProvider',
    'ExpressRouteServiceProviderBandwidthsOffered',
    'FlowLogInformation',
    'FlowLogStatusParameters',
    'FrontendIPConfiguration',
    'GatewayRoute',
    'GatewayRouteListResult',
    'HTTPConfiguration',
    'HTTPHeader',
    'InboundNatPool',
    'InboundNatRule',
    'IPAddressAvailabilityResult',
    'IPConfiguration',
    'IpsecPolicy',
    'IpTag',
    'Ipv6ExpressRouteCircuitPeeringConfig',
    'LoadBalancer',
    'LoadBalancerSku',
    'LoadBalancingRule',
    'LocalNetworkGateway',
    'LogSpecification',
    'MetricSpecification',
    'NetworkInterface',
    'NetworkInterfaceAssociation',
    'NetworkInterfaceDnsSettings',
    'NetworkInterfaceIPConfiguration',
    'NetworkSecurityGroup',
    'NetworkWatcher',
    'NextHopParameters',
    'NextHopResult',
    'Operation',
    'OperationDisplay',
    'OperationPropertiesFormatServiceSpecification',
    'OutboundNatRule',
    'PacketCapture',
    'PacketCaptureFilter',
    'PacketCaptureParameters',
    'PacketCaptureQueryStatusResult',
    'PacketCaptureResult',
    'PacketCaptureStorageLocation',
    'PatchRouteFilter',
    'PatchRouteFilterRule',
    'Probe',
    'ProtocolConfiguration',
    'PublicIPAddress',
    'PublicIPAddressDnsSettings',
    'PublicIPAddressSku',
    'QueryTroubleshootingParameters',
    'Resource',
    'ResourceNavigationLink',
    'RetentionPolicyParameters',
    'Route',
    'RouteFilter',
    'RouteFilterRule',
    'RouteTable',
    'SecurityGroupNetworkInterface',
    'SecurityGroupViewParameters',
    'SecurityGroupViewResult',
    'SecurityRule',
    'SecurityRuleAssociations',
    'ServiceEndpointPropertiesFormat',
    'Subnet',
    'SubnetAssociation',
    'SubResource',
    'TagsObject',
    'Topology',
    'TopologyAssociation',
    'TopologyParameters',
    'TopologyResource',
    'TroubleshootingDetails',
    'TroubleshootingParameters',
    'TroubleshootingRecommendedActions',
    'TroubleshootingResult',
    'TunnelConnectionHealth',
    'Usage',
    'UsageName',
    'VerificationIPFlowParameters',
    'VerificationIPFlowResult',
    'VirtualNetwork',
    'VirtualNetworkConnectionGatewayReference',
    'VirtualNetworkGateway',
    'VirtualNetworkGatewayConnection',
    'VirtualNetworkGatewayConnectionListEntity',
    'VirtualNetworkGatewayIPConfiguration',
    'VirtualNetworkGatewaySku',
    'VirtualNetworkPeering',
    'VirtualNetworkUsage',
    'VirtualNetworkUsageName',
    'VpnClientConfiguration',
    'VpnClientIPsecParameters',
    'VpnClientParameters',
    'VpnClientRevokedCertificate',
    'VpnClientRootCertificate',
    'VpnDeviceScriptParameters',
    'ApplicationGatewayPaged',
    'ApplicationGatewaySslPredefinedPolicyPaged',
    'ApplicationSecurityGroupPaged',
    'DdosProtectionPlanPaged',
    'EndpointServiceResultPaged',
    'ExpressRouteCircuitAuthorizationPaged',
    'ExpressRouteCircuitPeeringPaged',
    'ExpressRouteCircuitPaged',
    'ExpressRouteServiceProviderPaged',
    'ExpressRouteCrossConnectionPaged',
    'ExpressRouteCrossConnectionPeeringPaged',
    'LoadBalancerPaged',
    'BackendAddressPoolPaged',
    'FrontendIPConfigurationPaged',
    'InboundNatRulePaged',
    'LoadBalancingRulePaged',
    'NetworkInterfacePaged',
    'ProbePaged',
    'NetworkInterfaceIPConfigurationPaged',
    'NetworkSecurityGroupPaged',
    'SecurityRulePaged',
    'NetworkWatcherPaged',
    'PacketCaptureResultPaged',
    'ConnectionMonitorResultPaged',
    'OperationPaged',
    'PublicIPAddressPaged',
    'RouteFilterPaged',
    'RouteFilterRulePaged',
    'RouteTablePaged',
    'RoutePaged',
    'BgpServiceCommunityPaged',
    'UsagePaged',
    'VirtualNetworkPaged',
    'VirtualNetworkUsagePaged',
    'SubnetPaged',
    'VirtualNetworkPeeringPaged',
    'VirtualNetworkGatewayPaged',
    'VirtualNetworkGatewayConnectionListEntityPaged',
    'VirtualNetworkGatewayConnectionPaged',
    'LocalNetworkGatewayPaged',
    'TransportProtocol',
    'IPAllocationMethod',
    'IPVersion',
    'SecurityRuleProtocol',
    'SecurityRuleAccess',
    'SecurityRuleDirection',
    'RouteNextHopType',
    'PublicIPAddressSkuName',
    'ApplicationGatewayProtocol',
    'ApplicationGatewayCookieBasedAffinity',
    'ApplicationGatewayBackendHealthServerHealth',
    'ApplicationGatewaySkuName',
    'ApplicationGatewayTier',
    'ApplicationGatewaySslProtocol',
    'ApplicationGatewaySslPolicyType',
    'ApplicationGatewaySslPolicyName',
    'ApplicationGatewaySslCipherSuite',
    'ApplicationGatewayRequestRoutingRuleType',
    'ApplicationGatewayRedirectType',
    'ApplicationGatewayOperationalState',
    'ApplicationGatewayFirewallMode',
    'AuthorizationUseStatus',
    'ExpressRouteCircuitPeeringAdvertisedPublicPrefixState',
    'Access',
    'ExpressRoutePeeringType',
    'ExpressRoutePeeringState',
    'CircuitConnectionStatus',
    'ExpressRouteCircuitPeeringState',
    'ExpressRouteCircuitSkuTier',
    'ExpressRouteCircuitSkuFamily',
    'ServiceProviderProvisioningState',
    'LoadBalancerSkuName',
    'LoadDistribution',
    'ProbeProtocol',
    'NetworkOperationStatus',
    'EffectiveSecurityRuleProtocol',
    'EffectiveRouteSource',
    'EffectiveRouteState',
    'ProvisioningState',
    'AssociationType',
    'Direction',
    'IpFlowProtocol',
    'NextHopType',
    'PcProtocol',
    'PcStatus',
    'PcError',
    'Protocol',
    'HTTPMethod',
    'Origin',
    'Severity',
    'IssueType',
    'ConnectionStatus',
    'ConnectionMonitorSourceStatus',
    'ConnectionState',
    'EvaluationState',
    'VirtualNetworkPeeringState',
    'VirtualNetworkGatewayType',
    'VpnType',
    'VirtualNetworkGatewaySkuName',
    'VirtualNetworkGatewaySkuTier',
    'VpnClientProtocol',
    'IpsecEncryption',
    'IpsecIntegrity',
    'IkeEncryption',
    'IkeIntegrity',
    'DhGroup',
    'PfsGroup',
    'BgpPeerState',
    'ProcessorArchitecture',
    'AuthenticationMethod',
    'VirtualNetworkGatewayConnectionStatus',
    'VirtualNetworkGatewayConnectionType',
]
