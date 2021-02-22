======
ws_ui
======

A simple tui tool to communicate with websocket.

Motivation
===========

There are many cli/gui client tool for HTTP, like `cURL`, `httpie`, `Postman`, `Insomnia`.
But I cannot find one for websocket.

Install
=======

.. code::

    pip install ws-ui


Usage
======

Just call the command with websocket url. Then you can send and receive msg through a tui.

For example, we can run the `echo_server.py` and communicate with it.


.. code::

    $ python echo_server.py
    ======== Running on http://0.0.0.0:8080 ========
    (Press CTRL+C to quit)


.. code::

    $ ws-ui ws://localhost:8080


.. code:: 

    Enter msg and press Enter to send message

    * ['18:25:38'] connecting to ws://localhost:8080
    👌 ['18:25:38'] connected
    ⬇️ ['18:25:38'] ready

    ⬆️ ['18:26:35'] hello world 
    ⬇️ ['18:26:35'] received hello world











    ------------------------------------------------------
    input text here
