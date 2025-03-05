## Ubiquiti Unifi

To set up a portal for Unifi first we need to create a template. Then we have to add the Unifi controller which will be using that portal. A single template can be applied to multiple sites.

## Add a Unifi Controller

To add a Unifi Controller we will click on the New unifi controller button in the Unifi Controllers tab. An interactive wizard will launch. You need to enter the name, URL and username password for the Unifi Controller. It needs to be a local user with 2FA. The controller should be reachable directly over the internet using the provider hostname, not via ui.com portal.

![Unifi Wizard 1](../assets/images/unifi-wizard-1.png)

In the 2nd step the connection with the Unifi controller will be tested. If the connection is successful, we will get an option to assign sites on the Unifi controller to corresponding venues and templates on the Splash Admin Panel. You can use the `+` button at the bottom to add multiple sites.

![Unifi Wizard 2](../assets/images/unifi-wizard-2.png)

The 3rd and final step applies the settings for captive portal to the respective site on the Unifi controller. Click on the Create button to complete the process.

![Unifi Wizard 3](../assets/images/unifi-wizard-3.png)

Completing this process sets up the captive portal for the selected site(s) on the Admin Panel.

The controller will start showing on the Unifi Controllers page:

![Controller Added](../assets/images/controller-added.png)

You should check the site in the Unifi Controller to double check the captive portal settings. In Hotspot -> Authentication `External Portal Server` should be selected. 

![Unifi External Portal Server](../assets/images/unifi-external-portal-server.png)

By clicking on Edit you can view the IP address: it should show the IP address of the Splash Admin Panel server.

![Unifi Portal Server IP](../assets/images/unifi-portal-server-ip.png)

In the Settings tab the Landing Page Settings should be like this:

![Unifi Landing Page Settings](../assets/images/unifi-landing-page.png)

```
Show Landing Page: checked
HTTPs Redirection Support: unchecked
Encrypted URL: unchecked
Secure Portal: checked
Domain: checked

Domain: <Splash Admin Panel Domain>
```

## Portals

We can go to Portals to view the settings for the portal(s) just added.

![Unifi Portals](../assets/images/unifi-portals.png)

Clicking on a portal takes you to the details for that portal. It lets you specify additional settings:

```
Redirect URL: the URL a user is redirected to after succesful portal authorization
Business Name: name of the venue which will be displayed on top of the portal
Duration: the time in seconds for which a user is authorized on the network
```

You can click on the Edit button against each entry to modify it if needed.

![Unifi Portal Details](../assets/images/unifi-portal-details.png)