**Based on the needs_restarting.py module from Security Onion.**

https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/_modules/needs_restarting.py

Revision History:
* Robert Cooper <racooper@tamu.edu>
  - modified to use os_family and filter on osmajorrelease <=7 (RHEL)
  - renamed `check` to `check_reboot`, and added `check_services` functions.
