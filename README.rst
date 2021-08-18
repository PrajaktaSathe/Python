======
Python
======

This repository features various projects in Python - do check them out!

Give us a star if you find this useful!

************************************
Programs/Projects in this repository
************************************

Calculator
    This is a program which can implement basic mathematical operations (like addition, subtraction, multiplication, division etc.).

Dice Roll
    This program simulates the rolling of a 6-sided die. It shoots out random numbers from 1 to 6.

Guess the Number
    This is a simple one-player game that anyone can implement and play. The computer chooses a random number, which we have to guess in a specific number of guesses.

Leap year
    This is a simple program which takes user input and checks if the entered year is a leap year or not.

Madlibs
    A very simple and funny game. The computer/program asks the user to enter specific types of words (like nouns, pronouns etc.). The result is a fun script which you get to read and laugh at! (Console version of the standard Madlibs game!)

Contact list
    A program which stores, edits and displays phone numbers for users. I have tried to make it as user-friendly as possible!

Username generator
    A fun program which generates fun usernames.

URL Shortener
    A small program to shorten URLs!

Roshambo
    A small program to play Rock Paper Scissors.

Tkinter Calculator
    A Basic Calculator Program with GUI.

    .. image:: projects/sachinl0har/tkinter/images/calculator.png

Alpha
    A Virtual Assistant build in Python using pyttsx3, speech_recognition and some more, This Assistant can help you with your daily work on Laptop/PC By Providing you to give Talk Command.

Tkinter Digital Clock
    A Digital Clock built using Tkinter.

    .. image:: projects/sachinl0har/tkinter/images/digital_clock.png

Rock Paper Scissors Game
    Play rock paper scissors against the computer.

Acro
    A Talking AI ChatBot.

*****
Usage
*****

^^^^^^^^^^^^
Dependencies
^^^^^^^^^^^^

If you want run these programs make sure that you have Pipenv installed. You can get it using pip::

    pip install pipenv

When you are in the directory of a program you want to use, you can install any dependencies by running::

    pipenv install --ignore-pipfile

*********************
How can I contribute?
*********************

#. Create a Fork of this repository.
#. Create a folder in the *projects* directory and name it your username. Your projects go in that directory.
#. If your project consists of multiple files place them in a folder with the same name as the main file in the project.

***********************
Ideas for contributions
***********************

* If you have a project in Python that is not yet included in the repository, you can open up a PR.
* You can also open up a PR if you have a better way of coding (code enhancement) any of the projects in the repo!
* You can open an issue, if you see something like an error, or something buggy!
* Better documentation is also a great help to any repo! If you are one of those people who like to document stuff, this suggestion is for you!

**********************************************
What should I keep in mind while contributing?
**********************************************

* Make sure that the work is entirely your own and not from some other source.
* Make sure you are adding your project in the proper folder.

**************
For Developers
**************

^^^^^^^^^^^^^^^^
Dev Dependencies
^^^^^^^^^^^^^^^^

This repository uses Pipenv as its package manager; make sure to use that and not `pip`.

Pipenv saves other people that use your code the hassle of downloading all the dependencies manually.

^^^^^^^^^^^^^
Documentation
^^^^^^^^^^^^^

Please add useful documentation to your code so that others can easily understand it

.. code-block:: python

    # Use descriptive names for variables.
    def func(arg_1: type, arg_2: type, ...) -> type:
        """[Brief Description]

        :param arg_1: [Description of the Argument]
        :param arg_2:   [Description of the Argument]
        :return: [Description what the function Returns]
        """

**Note**: You don't need to include all that for all your functions, but try to always give a brief description.

Look at the other projects for examples.

*Ignore the rest of this section if you have never used sphinx before.*

This project uses sphinx for its documentation::

    pip install sphinx

You will probably also want to get the Read the Docs theme::

    pip install sphinx_rtd_theme

