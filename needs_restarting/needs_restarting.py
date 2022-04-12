# originally based on Security Onion's needs_restarting.py module
# https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/_modules/needs_restarting.py
'''
This module provides a way to check the reboot or service restart status
for a server. It checks reboot status for Ubuntu family and RedHat (7+) family, 
and checks service status for Redhat (7+). Requires yum-utils.
'''

from os import path
import subprocess

def check_reboot():
  '''
  Checks reboot status of server.  Returns True if server needs to be rebooted.
  '''
  os_family = __grains__['os_family']
  os_version = __grains__['osmajorrelease']
  retval = 'False'

  if os_family == 'Ubuntu':
    if path.exists('/var/run/reboot-required'):
      retval = 'True'

  elif os_family == 'RedHat':
    if os_version >= 7:
      cmd = 'needs-restarting -r > /dev/null 2>&1'
    
      try:
        needs_restarting = subprocess.check_call(cmd, shell=True)
      except subprocess.CalledProcessError:
        retval = 'True'
    else:
      retval = 'Unsupported OS version: %s' % os_version
  else:
    retval = 'Unsupported OS family: %s' % os_family

  return retval

def check_services():
  '''
  Checks for services that need to be restarted after an update.
  Returns a list of services that need restart, or nothing if clean.
  '''
  os_family = __grains__['os_family']
  os_version = __grains__['osmajorrelease']
  retval = 'False'

  if os_family == 'RedHat':
    if os_version >= 7:
      cmd = 'needs-restarting -s'
      needs_restarting = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
      retval = needs_restarting.stdout
    else:
      retval = 'Unsupported OS version: %s' % os_version
  else:
     retval = "Unsupported OS family: %s" % os_family
  return retval