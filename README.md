[![PyPI version](https://img.shields.io/pypi/v/geon-services-core)](https://pypi.org/project/geon-services-core)

This repository is created by modifying the beautiful, masterfully coded QWC Services Core repository 

QWC Services Core
=================

The QWC Services are a collection of microservices providing configurations for and authorized access to different QWC Map Viewer components.

See [QWC Docker](https://github.com/qwc-services/qwc-docker/) for using QWC Services with Docker.

This repository contains the shared modules for QWC services.


Development
===========

To use a local version of QWC Services Core for development, replace the
`qwc-services-core` module URL in `requirements.txt` of each service with an URL
pointing to the local files:

    # git+git://github.com/qwc-services/qwc-services-core.git#egg=qwc-services-core
    file:../qwc-services-core/#egg=qwc-services-core
