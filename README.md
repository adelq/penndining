PennDining Parser
=================

Preliminary attempt at programmatically fetching PennDining information.
Note: Your use of PennDining data may or may not be allowed. Use at your risk.

Team
----
Adel Qalieh -- Javascript -- @adelq
Prakhar Bhandari -- Python Backend -- @pbjr23
David Lakata -- Flask templating -- @dlakata

Technology
----------
HTML5, CSS3
Bootstrap
Normalize.css, jQuery, Moment.js
Python, Flask, BeautifulSoup

Getting Started
---------------
1. Install [virtualenv](http://www.virtualenv.org/) on your computer
2. Create a virtualenv for PennDining

    ```
    $ virtualenv penndining
    ```
3. Activate virtualenv

    ```
    $ cd penndining
    $ source bin/activate
    ```
4. Install Python module dependencies, namely `Flask` and `BeautifulSoup4`

    ```
    $ pip install flask BeautifulSoup4
    ```
5. Clone git repository into directory

    ```
    $ git clone https://github.com/adelq/penndining.git
    ```
6. Start server

    ```
    $ python penndining/app.py
    ```