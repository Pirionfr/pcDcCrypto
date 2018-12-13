
pyDcCrypto
==========

You can also download the source code and install it manually::

    cd /path/to/pyDcCrypto/
    python setup.py install


Usage
-----
encrypt your message

    pyDcCrypto -e -k <master key> -m <message>
    
decrypt your message

    pyDcCrypto -d -k <master key> -m <message>
    
Dev env
-------
create virtual env and install requirements

    virtualenv -p /usr/bin/python2.7 env
    pip install -r requirements.txt