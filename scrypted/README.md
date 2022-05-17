# Scrypted Add-on for Home Assistant

**THIS IS A WORK-IN-PROGRESS**

## About

This add-on allows you to set up Scrypted on your Home Assistant instance.

Scrypted offers many benefits, but perhaps its most useful function is providing super-low-latency HomeKit camera streaming and support for HomeKit Secure Video.

For more information about Scrypted, visit [the Scrypted website](https://scrypted.app).

## System requirements

- Home Assistant OS or Supervised installation running on aarch64, amd64 or armv7 architecture (if you have Home Assistant Core or Container installed then install Scrypted in a separate container using the instructions at [the Scrypted GitHub page](https://github.com/koush/scrypted).
- At least 2GB free storage space
- Raspberry Pi 4 or faster machine (performance noticeably worse on Raspberry Pi 3B)

## Installation

Add the repository [https://github.com/aegjoyce/ha-addons](https://github.com/aegjoyce/ha-addons) in Home Assistant (see [here](https://www.home-assistant.io/hassio/installing_third_party_addons/) for more information).

Then select the Scrypted add-on and click Install. **This may take 5-10 minutes to complete as the image is approximately 2GB in size.**

Once installed, make sure you enable Watchdog so that the Scrypted add-on will restart automatically if you need to restart Scrypted from within its UI.

Scrypted will then be accessible via **[YOUR_HOME_ASSISTANT_ADDRESS]:10443** - check the add-on logs after clicking 'Start' to confirm the server address.

You will likely need to approve a security/certificate message the first time you access Scrypted.

For external access, make sure you forward port 10443 to your Home Assistant instance on your router.

To export your configuration and database, make and download a backup of the Scrypted add-on. Data is stored in /scrypted_data.

## To-do

- Testing on different architectures to ensure compatibility (armv7 and amd64 are untested, and I have listed armhf and i386 as incompatible for now as the docker multi-arch image does not include these architectures)
- ~~WebUI support~~ - done
- Ingress support
- Apparmor support
- Try to get Scrypted to use Home Assistant certificates
- ~~Relocate Scrypted database to Config folder to allow for easier database editing/importing/exporting~~ - done
- ~~Proper implementation of changelog and versioning~~ - done
