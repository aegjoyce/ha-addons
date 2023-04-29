# Scrypted Lite Add-on for Home Assistant

For more information on Scrypted, please check out the [the Scrypted website](https://scrypted.app) or [the Scrypted GitHub page](https://github.com/koush/scrypted).

# Advanced: Environment variables
Environment variables may be set using the add-on configuration screen and are loaded as the add-on starts. Valid variables must begin with `SCRYPTED_`, for example:

```
- name: SCRYPTED_ADMIN_USERNAME
  value: false
- name: SCRYPTED_ADMIN_TOKEN
  value: homeassistant
- name: SCRYPTED_NVR_VOLUME
  value: homeassistant
```

The following environment variables can be set:
* `SCRYPTED_ADMIN_USERNAME`
  * Username used by Home Assistant to log in (default `homeassistant`)
* `SCRYPTED_ADMIN_TOKEN`
  * Password used by Home Assistant to log in (default `homeassistant`, change if you have security concerns)
* `SCRYPTED_NVR_VOLUME`
  * Sets the recording location for the NVR plugin (default `/data/scrypted_data/recordings`, excluded from add-on backups)
* `SCRYPTED_DISABLE_AUTHENTICATION`
  * Disables auth. Not recommended! Can be `true` or `false`
* `SCRYPTED_SECURE_PORT`
  * Sets the https port for accessing Scrypted outside of Ingress (default `10443`)
* `SCRYPTED_INSECURE_PORT`
  * Sets the http port for accessing Scrypted outside of Ingress (default `11080`)
* `SCRYPTED_HTTPS_OPTIONS_FILE`
  * Allows loading of a custom SSL certificate - follow the instructions [here](https://github.com/koush/scrypted/wiki/Custom-SSL-Certificate), put your JSON config file somewhere in the `config` folder and then set this variable to `/config/<yourJSONfile>`