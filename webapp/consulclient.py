"""
consul client
"""

import consul
import socket

HOST = 'consul'
IP_ADDRESS = socket.gethostbyname(socket.gethostname())

def register(port, tags, name):
    """
    register a new consul service
    """
    url = 'http://%s:%i/api/v1/health' % (IP_ADDRESS, port)
    http_check = consul.Check.http(interval='5s', url=url)
    return consul.Consul(host=HOST).agent.service.register(tags=tags, \
      name=name, \
      address=IP_ADDRESS, \
      port=port, \
      service_id='worker-%s' % IP_ADDRESS, \
      check=http_check)

def deregister():
    """
    deregister consul service
    """
    return consul.Consul(host=HOST).agent.service.deregister(service_id='worker-%s' % IP_ADDRESS)
