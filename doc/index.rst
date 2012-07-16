.. module:: sphinxcontrib.jinjadomain

:mod:`sphinxcontrib.jinjadomain` --- Documenting jinja templates
=================================================================

This contrib extension, :mod:`sphinxcontrib.jinjadomain`, provides a Sphinx
domain for describing jinja templates.

In order to use it, add :mod:`sphinxcontrib.jinjadomain` into
:data:`extensions` list of your Sphinx configuration file (:file:`conf.py`)::

    extensions = ['sphinxcontrib.jinjadomain']


Basic usage
-----------

There are several provided :ref:`directives <directives>` that describe
jinja templates.

.. sourcecode:: rst

   .. jinja:template:: /etc/network/interfaces

      Template for network config

      :param hostname: your computer's hostname
      :type hostname: str
      :param ip: your computer's ip
      :type ip: str

will be rendered as:

   .. jinja:template:: /etc/network/interfaces

      Template for network config

      :param hostname: your computer's hostname
      :type hostname: str
      :param ip: your computer's ip
      :type ip: st

.. _directives:

Directives
----------

.. rst:directive:: .. http:options:: path

   Describes a HTTP resource's :http:method:`OPTIONS` method.
   It can also be referred by :rst:role:`http:options` role.


.. _resource-fields:

Resource Fields
---------------

Inside HTTP resource description directives like :rst:dir:`get`,
reStructuredText field lists with these fields are recognized and formatted
nicely:

``param``, ``parameter``, ``arg``, ``argument``
   Description of URL parameter.

``queryparameter``, ``queryparam``, ``qparam``, ``query``
   Description of parameter passed by request query string.

``formparameter``, ``formparam``, ``fparam``, ``form``
   Description of parameter passed by request content body, encoded in
   :mimetype:`application/x-www-form-urlencoded` or
   :mimetype:`multipart/form-data`.

``statuscode``, ``status``, ``code``
   Description of response status code.

For example:

.. sourcecode:: rst

   .. http:post:: /posts/(int:post_id)

      Replies a comment to the post.

      :param post_id: post's unique id
      :type post_id: int
      :form email: author email address
      :form body: comment body
      :status 302: and then redirects to :http:get:`/posts/(int:post_id)`
      :status 400: when form parameters are missing

It will render like this:

    .. http:post:: /posts/(int:post_id)

       Replies a comment to the post.

       :param post_id: post's unique id
       :type post_id: int
       :form email: author email address
       :form body: comment body
       :status 302: and then redirects to :http:get:`/posts/(int:post_id)`
       :status 400: when form parameters are missing


.. module:: sphinxcontrib.autohttp.flask

:mod:`sphinxcontrib.autohttp.flask` --- Exporting API reference from Flask app
------------------------------------------------------------------------------

It generates RESTful HTTP API reference documentation from a Flask_
application's routing table, similar to :mod:`sphinx.ext.autodoc`.

In order to use it, add :mod:`sphinxcontrib.autohttp.flask` into
:data:`extensions` list of your Sphinx configuration (:file:`conf.py`) file::

    extensions = ['sphinxcontrib.autohttp.flask']

For example:

.. sourcecode:: rst

   .. autoflask:: autoflask_sampleapp:app
      :undoc-static:

will be rendered as:

    .. autoflask:: autoflask_sampleapp:app
       :undoc-static:

.. rst:directive:: .. autoflask:: module:app

   Generates HTTP API references from a Flask application. It takes an
   import name, like::

       your.webapplication.module:app

   Colon character (``:``) separates module path and application variable.
   Latter part can be more complex::

       your.webapplication.module:create_app(config='default.cfg')

   It's useful when a Flask application is created from the factory function
   (:func:`create_app`, in the above example).

   It takes several flag options as well.

   ``endpoints``
      Endpoints to generate a reference.

      .. sourcecode:: rst

         .. autoflask:: yourwebapp:app
            :endpoints: user, post, friends

      will document :func:`user`, :func:`post`, and :func:`friends`
      view functions, and

      .. sourcecode:: rst

         .. autoflask:: yourwebapp:app
            :endpoints:

      will document all endpoints in the flask app.

      For compatibility, omitting this option will produce the same effect
      like above.

   ``undoc-endpoints``
      Excludes specified endpoints from generated references.

      For example:

      .. sourcecode:: rst

         .. autoflask:: yourwebapp:app
            :undoc-endpoints: admin, admin_login

      will exclude :func:`admin`, :func:`admin_login` view functions.

      .. note::

         While the `undoc-members`_ flag of :mod:`sphinx.ext.autodoc` extension
         includes members without docstrings, ``undoc-endpoints`` option has
         nothing to do with docstrings. It just excludes specified endpoints.

         .. _undoc-members: http://sphinx.pocoo.org/ext/autodoc.html#directive-automodule

   ``undoc-static``
      Excludes a view function that serves static files, which is included
      in Flask by default.

   ``include-empty-docstring``
      View functions that don't have docstring (:attr:`__doc__`) are excluded
      by default. If this flag option has given, they become included also.

.. _Flask: http://flask.pocoo.org/


Author and License
------------------

The :mod:`sphinxcontrib.httpdomain` and :mod:`sphinxcontrib.autohttp`,
parts of :mod:`sphinxcontrib`, are written by `Hong Minhee`_
and distributed under BSD license.

The source code is mantained under `the common repository of contributed
extensions for Sphinx`__ (find the :file:`httpdomain` directory inside
the repository).

.. sourcecode:: console

   $ hg clone https://bitbucket.org/birkenfeld/sphinx-contrib
   $ cd sphinx-contrib/httpdomain

.. _Hong Minhee: http://dahlia.kr/
__ https://bitbucket.org/birkenfeld/sphinx-contrib

