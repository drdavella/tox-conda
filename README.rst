tox-conda
=========

`tox-conda` is a plugin that provides integration with the `conda
<https://conda.io>`_ package and environment manager for the `tox
<https://tox.readthedocs.io>`_ automation tool. It's like having your cake and
eating it, too!

By default, `tox` creates isolated environments using `virtualenv
<https://virtualenv.pypa.io>`_ and installs dependencies from `pip`.

In contrast, when using the `tox-conda` plugin `tox` will use `conda` to create
environments, and will install specified dependencies from `conda`. This is
useful for developers who rely on `conda` for environment management and
package distribution but want to take advantage of the features provided by
`tox` for test automation.

Installation
------------

Currently `tox-conda` can only be installed from source. A release on `pypi` is
expected in the near future.

To install from source, first clone the project from `github
<https://github.com/drdavella/tox-conda>`_:

::

   $ git clone https://github.com/drdavella/tox-conda

Then install it in your environment:

::

   $ cd tox-conda
   $ pip install .

To install in `development
mode <https://packaging.python.org/tutorials/distributing-packages/#working-in-development-mode>`__::

   $ pip install -e .

The `tox-conda` plugin expects that `tox` and `conda` are already installed and
available in your working environment.

Usage
-----

Details on `tox` usage can be found in the `tox documentation
<https://tox.readthedocs.io>`_.

With the plugin installed and no other changes, the `tox-conda` plugin will use
`conda` to create environments and use `pip` to install dependencies that are
given in the `tox.ini` configuration file.

`tox-conda` adds two additional (and optional) settings to the `[testenv]`
section of configuration files:

* `conda_deps`, which is used to configure which dependencies are installed
  from `conda` instead of from `pip`. All dependencies in `conda_deps` are
  installed before all dependencies in `deps`. If not given, no dependencies
  will be installed using `conda`.

* `conda_channels`, which specifies which channel(s) should be used for
  resolving `conda` dependencies. If not given, only the `default` channel will
  be used.

An example configuration file is given below:

::

   [tox]
   envlist =
       {py35,py36,py37}-{stable,dev}

   [testenv]
   deps=
       pytest-sugar
       py35,py36: importlib_resources
       dev: git+git://github.com/numpy/numpy
   conda_deps=
       pytest<=3.8
       stable: numpy=1.15
   conda_channels=
       conda-forge
   commands=
       pytest {posargs}

More information on `tox` configuration files can be found in the
`documentation <https://tox.readthedocs.io/en/latest/config.html>`_.
