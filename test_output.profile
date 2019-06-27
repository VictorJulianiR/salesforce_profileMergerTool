<?xml version="1.0" encoding="UTF-8"?>
<Profile xmlns="http://soap.sforce.com/2006/04/metadata">
    <applicationVisibilities>
        <application>CustomApp1</application>
        <default>false</default>
        <visible>true</visible>
    </applicationVisibilities>
    <applicationVisibilities>
        <application>CustomApp2</application>
        <default>true</default>
        <visible>true</visible>
    </applicationVisibilities>
    <applicationVisibilities>
        <application>CustomApp3</application>
        <default>true</default>
        <visible>true</visible>
    </applicationVisibilities>
    <classAccesses>
        <apexClass>AwesomeCustomClass1</apexClass>
        <enabled>true</enabled>
    </classAccesses>
    <classAccesses>
        <apexClass>AwesomeCustomClass2</apexClass>
        <enabled>true</enabled>
    </classAccesses>
    <custom>true</custom>
    <fieldPermissions>
        <editable>false</editable>
        <field>Account.AccountNumber</field>
        <readable>false</readable>
    </fieldPermissions>
    <fieldPermissions>
        <editable>false</editable>
        <field>Account.AnnualRevenue</field>
        <readable>false</readable>
    </fieldPermissions>
    <layoutAssignments>
        <layout>Account - Account Layout</layout>
    </layoutAssignments>
    <layoutAssignments>
        <layout>Account-Business Account Layout</layout>
        <recordType>Account.CustomRT</recordType>
    </layoutAssignments>
    <objectPermissions>
        <allowCreate>true</allowCreate>
        <allowDelete>true</allowDelete>
        <allowEdit>true</allowEdit>
        <allowRead>true</allowRead>
        <modifyAllRecords>true</modifyAllRecords>
        <object>Account</object>
        <viewAllRecords>true</viewAllRecords>
    </objectPermissions>
    <objectPermissions>
        <allowCreate>true</allowCreate>
        <allowDelete>false</allowDelete>
        <allowEdit>true</allowEdit>
        <allowRead>true</allowRead>
        <modifyAllRecords>false</modifyAllRecords>
        <object>Asset</object>
        <viewAllRecords>false</viewAllRecords>
    </objectPermissions>
    <objectPermissions>
        <allowCreate>true</allowCreate>
        <allowDelete>false</allowDelete>
        <allowEdit>true</allowEdit>
        <allowRead>true</allowRead>
        <modifyAllRecords>false</modifyAllRecords>
        <object>Case</object>
        <viewAllRecords>false</viewAllRecords>
    </objectPermissions>
    <pageAccesses>
        <apexPage>viewContact</apexPage>
        <enabled>true</enabled>
    </pageAccesses>
    <pageAccesses>
        <apexPage>viewAccount</apexPage>
        <enabled>false</enabled>
    </pageAccesses>
    <profileActionOverrides>
        <actionName>Tab</actionName>
        <content>HomePageAnalysts</content>
        <formFactor>Large</formFactor>
        <pageOrSobjectType>standard-home</pageOrSobjectType>
        <type>Flexipage</type>
    </profileActionOverrides>
    <recordTypeVisibilities>
        <default>false</default>
        <personAccountDefault>false</personAccountDefault>
        <recordType>Account.CustomRT</recordType>
        <visible>false</visible>
    </recordTypeVisibilities>
    <recordTypeVisibilities>
        <default>true</default>
        <personAccountDefault>false</personAccountDefault>
        <recordType>Account.CustomRT2</recordType>
        <visible>true</visible>
    </recordTypeVisibilities>
    <tabVisibilities>
        <tab>standard-Account</tab>
        <visibility>DefaultOn</visibility>
    </tabVisibilities>
    <tabVisibilities>
        <tab>standard-Asset</tab>
        <visibility>DefaultOn</visibility>
    </tabVisibilities>
    <tabVisibilities>
        <tab>standard-Case</tab>
        <visibility>DefaultOn</visibility>
    </tabVisibilities>
    <tabVisibilities>
        <tab>standard-Contact</tab>
        <visibility>DefaultOn</visibility>
    </tabVisibilities>
    <tabVisibilities>
        <tab>standard-Entitlement</tab>
        <visibility>DefaultOn</visibility>
    </tabVisibilities>
    <tabVisibilities>
        <tab>standard-Lead</tab>
        <visibility>DefaultOn</visibility>
    </tabVisibilities>
    <tabVisibilities>
        <tab>standard-Opportunity</tab>
        <visibility>DefaultOn</visibility>
    </tabVisibilities>
    <tabVisibilities>
        <tab>standard-Pricebook2</tab>
        <visibility>DefaultOff</visibility>
    </tabVisibilities>
    <tabVisibilities>
        <tab>standard-Product2</tab>
        <visibility>DefaultOn</visibility>
    </tabVisibilities>
    <tabVisibilities>
        <tab>standard-Quote</tab>
        <visibility>DefaultOn</visibility>
    </tabVisibilities>
    <userLicense>Salesforce</userLicense>
    <userPermissions>
        <enabled>false</enabled>
        <name>ActivateContract</name>
    </userPermissions>
    <userPermissions>
        <enabled>true</enabled>
        <name>ActivateOrder</name>
    </userPermissions>
    <userPermissions>
        <enabled>true</enabled>
        <name>ActivitiesAccess</name>
    </userPermissions>
    <userPermissions>
        <enabled>true</enabled>
        <name>AddDirectMessageMembers</name>
    </userPermissions>
    <userPermissions>
        <enabled>false</enabled>
        <name>AllowUniversalSearch</name>
    </userPermissions>
    <applicationVisibilities>
        <application>CustomApp4</application>
        <default>true</default>
        <visible>true</visible>
    </applicationVisibilities>
    <fieldPermissions>
        <editable>true</editable>
        <field>Account.AccountSource</field>
        <readable>true</readable>
    </fieldPermissions>
    <layoutAssignments>
        <layout>Account-Business Account Layout</layout>
    </layoutAssignments>
    <layoutAssignments>
        <layout>Account-Business Account Layout</layout>
        <recordType>Account.CustomRT2</recordType>
    </layoutAssignments>
</Profile>