# Scrypted Add-on for Home Assistant

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Faegjoyce%2Fha-addons)
![stars](https://img.shields.io/github/stars/aegjoyce/ha-addons?color=gold&style=for-the-badge)

![version](https://img.shields.io/github/v/release/aegjoyce/ha-addons?color=blue&style=flat-square)
![supported](https://img.shields.io/badge/supported-aarch64%20%7C%20amd64%20%7C%20armv7-green?style=flat-square)
![unsupported](https://img.shields.io/badge/unsupported-armhf%20%7C%20i386-red?style=flat-square)

## About

This add-on allows you to set up Scrypted on your Home Assistant instance.

Scrypted offers many benefits, but perhaps its most useful function is providing super-low-latency HomeKit camera streaming and support for HomeKit Secure Video.

For more information about Scrypted, visit [the Scrypted website](https://scrypted.app).

Not sure which Scrypted to install? Click [here](https://github.com/koush/scrypted/wiki/Docker-Image-Tags) to find out the differences between the Full, Lite and Thin versions.

## System requirements

- Home Assistant OS or Supervised installation running on aarch64, amd64 or armv7 architecture (if you have Home Assistant Core or Container installed then install Scrypted in a separate container using the instructions at [the Scrypted GitHub page](https://github.com/koush/scrypted))
- At least 2GB free storage space
- Raspberry Pi 4 or faster machine (performance noticeably worse on Raspberry Pi 3B)

## Installation

Add the repository [https://github.com/aegjoyce/ha-addons](https://github.com/aegjoyce/ha-addons) in Home Assistant (see [here](https://www.home-assistant.io/hassio/installing_third_party_addons/) for more information).

Then select the Scrypted add-on and click Install.

Once installed, make sure you enable Watchdog so that the Scrypted add-on will restart automatically if you need to restart Scrypted from within its UI, and add Scrypted to the sidebar.

Scrypted will then be accessible via the icon in the sidebar, or at `[YOUR_HOME_ASSISTANT_ADDRESS_OR_IP]:10443` - check the add-on logs after clicking 'Start' to confirm the server address.

To export your configuration and database, make and download a backup of the Scrypted add-on. Data is stored in `/scrypted_data`.

## Backup

Scrypted server files and NVR recordings will not be backed up in order to reduce backup size and time. User configuration and database will be backed up. If backups are getting too big then exclude the add-on from your routine backups.

## Import and export

It is possible to import an existing Scrypted configuation into the add-on by following this procedure:
1. Make a partial Home Assistant backup of the Scrypted add-on
2. Download the backup and delete it from Home Assistant
3. Extract the contents of the add-on and replace the contents of `/scrypted_data` with the database and configuration files you want to import
4. Re-compress the backup into a `.tar.gz` and re-upload to Home Assistant (Settings/System/Backups/Upload backup)
5. Restore the backup

To export your Scrypted configuration, follow steps 1-3 and copy the contents of `/scrypted_data` to your new Scrypted instance.

## Known issues

- Clicking 'Scrypted' in the top left will re-open your Home Assistant dashboard within the Ingress frame
- Some functions (external links, logins, etc.) are not yet optimised for Ingress - if something isn't working, try setting it up via `[YOUR_HOME_ASSISTANT_ADDRESS_OR_IP]:10443`.