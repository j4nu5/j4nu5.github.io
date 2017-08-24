Pelican Setup
#############

:date: 2017-08-24
:tags: setup
:category: Random
:authors: Kushagra Sinha


Install Pelican:

.. code-block:: shell

   sudo -H pip install pelican Markdown typogrify


Install Pelican themes

.. code-block:: shell

   git clone --recursive https://github.com/getpelican/pelican-themes
   sudo /usr/local/bin/pelican-themes --install pelican-themes/Flex
   sudo chmod 755 /usr/local/lib/python2.7/dist-packages/pelican/themes/Flex


Install Pelican plugins

.. code-block:: shell

   git clone --recursive https://github.com/getpelican/pelican-plugins


Fetch blog sources

.. code-block:: shell

   git clone git@github.com:j4nu5/j4nu5.github.io.git
   cd j4nu5.github.io.git
   git fetch
   git checkout source


Setup for development

.. code-block:: shell

   mkdir cache output


Verify plugins root

.. code-block:: shell

   grep PLUGIN_PATHS pelicanconf.py


Install Github pages

.. code-block:: shell

   sudo -H pip install ghp-import


Check out the scripts and the Makefile
