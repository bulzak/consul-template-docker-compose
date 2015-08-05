# Flask webapp

Simple Python 2.7 web application built with Flask framework.

It makes use of a Consul client (python-consul) to register the webapp when starting and then deregister it when shutting down the application.

The application also register a Consul HTTP Health-check to ensure that the service is active.