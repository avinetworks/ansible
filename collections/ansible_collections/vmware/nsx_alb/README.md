# Ansible Collection: vmware.nsx_alb

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
<!--end requires_ansible-->

## Installation and Usage

### Installing the Collection from Ansible Galaxy

Before using the VMware community collection, you need to install the collection with the `ansible-galaxy` CLI:

    ansible-galaxy collection install vmware.nsx_alb

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
- name: vmware.nsx_alb
```

### Required Python libraries

Nsx alb community collection depends upon following third party libraries:

* [`Avisdk`](https://github.com/avinetworks/sdk) >= 18.2.8

### Installing required libraries and SDK

Installing collection does not install any required third party Python libraries or SDKs. You need to install the required Python libraries using following command:

    pip install -r ~/.ansible/collections/ansible_collections/vmware/nsx_alb/requirements.txt

### Modules
Name | Description
--- | ---
[vmware.nsx_alb.avi_tenant](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_tenant,rst)|Module to create update or delete Tenant
[vmware.nsx_alb.avi_albservicesconfig](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_albservicesconfig,rst)|Module to create update or delete ALBServicesConfig
[vmware.nsx_alb.avi_systemlimits](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_systemlimits,rst)|Module to create update or delete SystemLimits
[vmware.nsx_alb.avi_licenseledgerdetails](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_licenseledgerdetails,rst)|Module to create update or delete LicenseLedgerDetails
[vmware.nsx_alb.avi_controllerproperties](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_controllerproperties,rst)|Module to create update or delete ControllerProperties
[vmware.nsx_alb.avi_useraccountprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_useraccountprofile,rst)|Module to create update or delete UserAccountProfile
[vmware.nsx_alb.avi_cloudproperties](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_cloudproperties,rst)|Module to create update or delete CloudProperties
[vmware.nsx_alb.avi_seproperties](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_seproperties,rst)|Module to create update or delete SeProperties
[vmware.nsx_alb.avi_cloudconnectoruser](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_cloudconnectoruser,rst)|Module to create update or delete CloudConnectorUser
[vmware.nsx_alb.avi_hardwaresecuritymodulegroup](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_hardwaresecuritymodulegroup,rst)|Module to create update or delete HardwareSecurityModuleGroup
[vmware.nsx_alb.avi_alertscriptconfig](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_alertscriptconfig,rst)|Module to create update or delete AlertScriptConfig
[vmware.nsx_alb.avi_customipamdnsprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_customipamdnsprofile,rst)|Module to create update or delete CustomIpamDnsProfile
[vmware.nsx_alb.avi_networkprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_networkprofile,rst)|Module to create update or delete NetworkProfile
[vmware.nsx_alb.avi_stringgroup](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_stringgroup,rst)|Module to create update or delete StringGroup
[vmware.nsx_alb.avi_ipaddrgroup](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_ipaddrgroup,rst)|Module to create update or delete IpAddrGroup
[vmware.nsx_alb.avi_pkiprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_pkiprofile,rst)|Module to create update or delete PKIProfile
[vmware.nsx_alb.avi_sslprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_sslprofile,rst)|Module to create update or delete SSLProfile
[vmware.nsx_alb.avi_applicationpersistenceprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_applicationpersistenceprofile,rst)|Module to create update or delete ApplicationPersistenceProfile
[vmware.nsx_alb.avi_alertemailconfig](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_alertemailconfig,rst)|Module to create update or delete AlertEmailConfig
[vmware.nsx_alb.avi_snmptrapprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_snmptrapprofile,rst)|Module to create update or delete SnmpTrapProfile
[vmware.nsx_alb.avi_autoscalelaunchconfig](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_autoscalelaunchconfig,rst)|Module to create update or delete AutoScaleLaunchConfig
[vmware.nsx_alb.avi_fileobject](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_fileobject,rst)|Module to create update or delete FileObject
[vmware.nsx_alb.avi_securitypolicy](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_securitypolicy,rst)|Module to create update or delete SecurityPolicy
[vmware.nsx_alb.avi_protocolparser](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_protocolparser,rst)|Module to create update or delete ProtocolParser
[vmware.nsx_alb.avi_jwtserverprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_jwtserverprofile,rst)|Module to create update or delete JWTServerProfile
[vmware.nsx_alb.avi_wafprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_wafprofile,rst)|Module to create update or delete WafProfile
[vmware.nsx_alb.avi_wafapplicationsignatureprovider](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_wafapplicationsignatureprovider,rst)|Module to create update or delete WafApplicationSignatureProvider
[vmware.nsx_alb.avi_errorpagebody](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_errorpagebody,rst)|Module to create update or delete ErrorPageBody
[vmware.nsx_alb.avi_testsedatastorelevel3](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_testsedatastorelevel3,rst)|Module to create update or delete TestSeDatastoreLevel3
[vmware.nsx_alb.avi_botconfigconsolidator](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_botconfigconsolidator,rst)|Module to create update or delete BotConfigConsolidator
[vmware.nsx_alb.avi_federationcheckpoint](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_federationcheckpoint,rst)|Module to create update or delete FederationCheckpoint
[vmware.nsx_alb.avi_gslbgeodbprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_gslbgeodbprofile,rst)|Module to create update or delete GslbGeoDbProfile
[vmware.nsx_alb.avi_siteversion](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_siteversion,rst)|Module to create update or delete SiteVersion
[vmware.nsx_alb.avi_image](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_image,rst)|Module to create update or delete Image
[vmware.nsx_alb.avi_controllerportalregistration](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_controllerportalregistration,rst)|Module to create update or delete ControllerPortalRegistration
[vmware.nsx_alb.avi_dynamicdnsrecord](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_dynamicdnsrecord,rst)|Module to create update or delete DynamicDnsRecord
[vmware.nsx_alb.avi_controllersite](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_controllersite,rst)|Module to create update or delete ControllerSite
[vmware.nsx_alb.avi_role](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_role,rst)|Module to create update or delete Role
[vmware.nsx_alb.avi_albservicesfileupload](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_albservicesfileupload,rst)|Module to create update or delete ALBServicesFileUpload
[vmware.nsx_alb.avi_webhook](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_webhook,rst)|Module to create update or delete Webhook
[vmware.nsx_alb.avi_securitymanagerdata](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_securitymanagerdata,rst)|Module to create update or delete SecurityManagerData
[vmware.nsx_alb.avi_cluster](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_cluster,rst)|Module to create update or delete Cluster
[vmware.nsx_alb.avi_poolgroupdeploymentpolicy](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_poolgroupdeploymentpolicy,rst)|Module to create update or delete PoolGroupDeploymentPolicy
[vmware.nsx_alb.avi_backupconfiguration](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_backupconfiguration,rst)|Module to create update or delete BackupConfiguration
[vmware.nsx_alb.avi_clusterclouddetails](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_clusterclouddetails,rst)|Module to create update or delete ClusterCloudDetails
[vmware.nsx_alb.avi_certificatemanagementprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_certificatemanagementprofile,rst)|Module to create update or delete CertificateManagementProfile
[vmware.nsx_alb.avi_ipamdnsproviderprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_ipamdnsproviderprofile,rst)|Module to create update or delete IpamDnsProviderProfile
[vmware.nsx_alb.avi_analyticsprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_analyticsprofile,rst)|Module to create update or delete AnalyticsProfile
[vmware.nsx_alb.avi_wafpolicypsmgroup](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_wafpolicypsmgroup,rst)|Module to create update or delete WafPolicyPSMGroup
[vmware.nsx_alb.avi_botmapping](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_botmapping,rst)|Module to create update or delete BotMapping
[vmware.nsx_alb.avi_natpolicy](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_natpolicy,rst)|Module to create update or delete NatPolicy
[vmware.nsx_alb.avi_applicationprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_applicationprofile,rst)|Module to create update or delete ApplicationProfile
[vmware.nsx_alb.avi_microservicegroup](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_microservicegroup,rst)|Module to create update or delete MicroServiceGroup
[vmware.nsx_alb.avi_ipreputationdb](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_ipreputationdb,rst)|Module to create update or delete IPReputationDB
[vmware.nsx_alb.avi_geodb](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_geodb,rst)|Module to create update or delete GeoDB
[vmware.nsx_alb.avi_errorpageprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_errorpageprofile,rst)|Module to create update or delete ErrorPageProfile
[vmware.nsx_alb.avi_testsedatastorelevel2](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_testsedatastorelevel2,rst)|Module to create update or delete TestSeDatastoreLevel2
[vmware.nsx_alb.avi_gslb](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_gslb,rst)|Module to create update or delete Gslb
[vmware.nsx_alb.avi_upgradestatusinfo](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_upgradestatusinfo,rst)|Module to create update or delete UpgradeStatusInfo
[vmware.nsx_alb.avi_upgradestatussummary](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_upgradestatussummary,rst)|Module to create update or delete UpgradeStatusSummary
[vmware.nsx_alb.avi_scheduler](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_scheduler,rst)|Module to create update or delete Scheduler
[vmware.nsx_alb.avi_sslkeyandcertificate](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_sslkeyandcertificate,rst)|Module to create update or delete SSLKeyAndCertificate
[vmware.nsx_alb.avi_networksecuritypolicy](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_networksecuritypolicy,rst)|Module to create update or delete NetworkSecurityPolicy
[vmware.nsx_alb.avi_botdetectionpolicy](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_botdetectionpolicy,rst)|Module to create update or delete BotDetectionPolicy
[vmware.nsx_alb.avi_testsedatastorelevel1](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_testsedatastorelevel1,rst)|Module to create update or delete TestSeDatastoreLevel1
[vmware.nsx_alb.avi_backup](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_backup,rst)|Module to create update or delete Backup
[vmware.nsx_alb.avi_cloud](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_cloud,rst)|Module to create update or delete Cloud
[vmware.nsx_alb.avi_healthmonitor](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_healthmonitor,rst)|Module to create update or delete HealthMonitor
[vmware.nsx_alb.avi_alertsyslogconfig](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_alertsyslogconfig,rst)|Module to create update or delete AlertSyslogConfig
[vmware.nsx_alb.avi_vrfcontext](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_vrfcontext,rst)|Module to create update or delete VrfContext
[vmware.nsx_alb.avi_vcenterserver](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_vcenterserver,rst)|Module to create update or delete VCenterServer
[vmware.nsx_alb.avi_prioritylabels](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_prioritylabels,rst)|Module to create update or delete PriorityLabels
[vmware.nsx_alb.avi_nsxtsegmentruntime](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_nsxtsegmentruntime,rst)|Module to create update or delete NsxtSegmentRuntime
[vmware.nsx_alb.avi_gslbservice](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_gslbservice,rst)|Module to create update or delete GslbService
[vmware.nsx_alb.avi_actiongroupconfig](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_actiongroupconfig,rst)|Module to create update or delete ActionGroupConfig
[vmware.nsx_alb.avi_availabilityzone](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_availabilityzone,rst)|Module to create update or delete AvailabilityZone
[vmware.nsx_alb.avi_alertconfig](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_alertconfig,rst)|Module to create update or delete AlertConfig
[vmware.nsx_alb.avi_serverautoscalepolicy](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_serverautoscalepolicy,rst)|Module to create update or delete ServerAutoScalePolicy
[vmware.nsx_alb.avi_network](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_network,rst)|Module to create update or delete Network
[vmware.nsx_alb.avi_serviceenginegroup](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_serviceenginegroup,rst)|Module to create update or delete ServiceEngineGroup
[vmware.nsx_alb.avi_pool](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_pool,rst)|Module to create update or delete Pool
[vmware.nsx_alb.avi_trafficcloneprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_trafficcloneprofile,rst)|Module to create update or delete TrafficCloneProfile
[vmware.nsx_alb.avi_vsvip](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_vsvip,rst)|Module to create update or delete VsVip
[vmware.nsx_alb.avi_serviceengine](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_serviceengine,rst)|Module to create update or delete ServiceEngine
[vmware.nsx_alb.avi_networkservice](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_networkservice,rst)|Module to create update or delete NetworkService
[vmware.nsx_alb.avi_poolgroup](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_poolgroup,rst)|Module to create update or delete PoolGroup
[vmware.nsx_alb.avi_pingaccessagent](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_pingaccessagent,rst)|Module to create update or delete PingAccessAgent
[vmware.nsx_alb.avi_httppolicyset](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_httppolicyset,rst)|Module to create update or delete HTTPPolicySet
[vmware.nsx_alb.avi_dnspolicy](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_dnspolicy,rst)|Module to create update or delete DnsPolicy
[vmware.nsx_alb.avi_vsdatascriptset](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_vsdatascriptset,rst)|Module to create update or delete VSDataScriptSet
[vmware.nsx_alb.avi_l4policyset](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_l4policyset,rst)|Module to create update or delete L4PolicySet
[vmware.nsx_alb.avi_icapprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_icapprofile,rst)|Module to create update or delete IcapProfile
[vmware.nsx_alb.avi_authprofile](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_authprofile,rst)|Module to create update or delete AuthProfile
[vmware.nsx_alb.avi_ssopolicy](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_ssopolicy,rst)|Module to create update or delete SSOPolicy
[vmware.nsx_alb.avi_systemconfiguration](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_systemconfiguration,rst)|Module to create update or delete SystemConfiguration
[vmware.nsx_alb.avi_virtualservice](https://github.com/avinetworks/ansible/blob/ansible_collection/collections/ansible_collections/vmware/nsx_alb/docs/avi_virtualservice,rst)|Module to create update or delete VirtualService
<!--end collection content-->

### Testing with `ansible-test`

Refer [testing](testing.md) for more information.

## Publishing New Version

Examples
--------

    - name: Example to create create Pool object
      vmware.nsx_alb.avi_pool:
        controller: "10.79.16.13"
        username: "admin"
        password: "password"
        name: app1-pool
        lb_algorithm: LB_ALGORITHM_LEAST_LOAD
        servers:
        - ip:
             addr: 10.90.64.22
             type: 'V4'