## Setting up Templates

In the Templates tab you can add a new template using the New template button or through the Import button if you have a previous export that you'd like to import.

When creating a new template you can modify the logo and the text fields according to your preference. The field selector section allows you to enable/disable various fields like Email and Phone number based on your requirements. You can change the font, button color, and placeholders for fields. Also, you can add a Background Image. The changes will be displayed in real time on the panel on the right side.

![Template](assets/images/template.png)

## Flow

There are 2 types of user authorization flows that are currently supported:

 - Simple
 - OTP

### Simple Flow

In Simple Flow the user enters their email and mobile number data but does not have to go through OTP based verification.

Here is an example of Simple flow:

<iframe width="560" height="315" 
    src="https://www.youtube.com/embed/K6QrtRPBBg4" 
    frameborder="0" allowfullscreen>
</iframe>

### OTP Flow

In OTP Flow the user has to verify their data using an OTP (One Time Password). You can setup either email verification or mobile number verification.

Here is an example of OTP flow:

<iframe width="560" height="315" 
    src="https://www.youtube.com/embed/yRG6ERp7FDg" 
    frameborder="0" allowfullscreen>
</iframe>

### Email Based OTP Verification Caveat

Implementing email based OTP verification is not recommended. A user in captive state does not have complete internet access, so they will not be able to check their email on the same device. Either they would need another device to check their email, or they would need to have cellular internet on the same device to receive email via that. Additionally, on iOS devices the Captive Network Assistant (CNA) launches a browser that does not allow switching to another window. If you switch to a different window for checking email the browser will close.

Therefore, keep these limitations in mind when implementing email based OTP verifications.

## Preview Template

You can click on the preview changes button on the top right to view a full screen preview for mobile, tablet and desktop in portrait and landscape orientation.

![Preview Changes](assets/images/preview-changes.png)

In the full screen preview you can use the buttons on the top to toggle between mobile, tablet and desktop view and switch orientation between portrait and landscape. This lets you visualize the captive portal as users will see it.

![Full Preview](assets/images/full-preview.png)