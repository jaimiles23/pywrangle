=========
PyWrangle
=========

PyWrangle is an open-source Python library for data wrangling. Wikipedia defines `data wrangling <https://en.wikipedia.org/wiki/Data_wrangling>`_ as follows:

**Data Wrangling**
   is the process of transforming and mapping data from one "raw" data form into another format with the intent of making it more appropriate and valuable for a variety of downstream purposes such as analytics


PyWrangle helps:

- Clean strings
- Track DataFrame changes
- Identify & correct string data entry errors

PyWrangle is available on `PyPI <https://pypi.org/project/pywrangle/>`_


Table of Contents
-----------------

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   modules


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`


Install & Requirements
----------------------

Install
^^^^^^^

PyWrangle can be installed with pip.

::

   python -m pip install pywrangle


Requirements
^^^^^^^^^^^^

- Python >= 3.8+
- numpy >= 1.14.4
- pandas >= 1.0.3
- fuzzywuzzy >= 0.18.0
- python-levenshtein >= 0.12.0
- metaphone >= 0.6


Convention
----------
Per convention with Python libraries for data science, import pywrangle as follows:

.. code-block:: python

   >>> import pywrangle as pw 


GitHub
------

Please feel free to contribute to PyWrangle! `GitHub <https://github.com/jaimiles23/pywrangle>`_

:Authors:
   Jai Miles
:Version:
   0.3
:Dedication:
   To everyone who just wanted clean data ~