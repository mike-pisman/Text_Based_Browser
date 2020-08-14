# Text-Based Browser in Python
### About
Sometimes you need to read online documentation or find something on the Internet from the command line or terminal. So, let's use Python to create a text-based browser! Of course, making a real, full-blown browser is a very difficult task. In this project, you'll create a very simple browser that will ignore JavaScript and CSS, won't have cookies, and will only process a limited set of tags. Still, it will be useful and, most importantly, fun to program!

### Learning outcomes
I learnt how HTTP works and how to handle its protocols using Python. I also learnt all about Python input/output, as well as parsing HTML, got to know BeatifulSoup  and Colormap libraries.

### Functions
 - The program accepts commands and URLs of websites
 - The program downloads page from given URL in CLI
 - The program then parses the html page, extracts all the text and prints it to CLI
 - The program prints links in blue and regular text in white
 - The program has a simlple history and can print already visited pages using short name

### CLI arguments
The programm accepts 1 CLI argument - name of the folder to use for saved pages, if no name is passed, the programm will create default ```tmp``` folder in the root directory and delete it on ```exit``` command

**Example:**
```python browser.py name_of_directory``` will create directory with name "name_of_directory"
```python browser.py```  will create default directory with name "tmp"

### Menu commands
```
 - url of the page you would like to visit
 - "back" to print previously visited page
 - "exit" to exit the program
```

### Example of running programm
```
> https://docs.python.org
index
modules
Python
Documentation
Python 3.7.4 documentation
Welcome! This is the documentation for Python 3.7.4.
Parts of the documentation:
What's new in Python 3.7? or all "What's new" documents since 2.0
Tutorial start here
Library Reference keep this under your pillow
Language Reference describes syntax and language elements
Python Setup and Usage how to use Python on different platforms
Python HOWTOs in-depth documents on specific topics
Installing Python Modules installing from the Python Package Index & other sources
Distributing Python Modules publishing modules for installation by others
Extending and Embedding tutorial for C/C++ programmers
Python/C API reference for C/C++ programmers
FAQs frequently asked questions (with answers!)
Indices and tables:
Global Module Index quick access to all modules
General Index all functions, classes, terms
Glossary the most important terms explained
Search page search this documentation
Complete Table of Contents lists all sections and subsections
Meta information:
Reporting bugs
About the documentation
History and License of Python
Copyright
> docs.python
index
modules
Python
Documentation
Python 3.7.4 documentation
Welcome! This is the documentation for Python 3.7.4.
Parts of the documentation:
What's new in Python 3.7? or all "What's new" documents since 2.0
Tutorial start here
Library Reference keep this under your pillow
Language Reference describes syntax and language elements
Python Setup and Usage how to use Python on different platforms
Python HOWTOs in-depth documents on specific topics
Installing Python Modules installing from the Python Package Index & other sources
Distributing Python Modules publishing modules for installation by others
Extending and Embedding tutorial for C/C++ programmers
Python/C API reference for C/C++ programmers
FAQs frequently asked questions (with answers!)
Indices and tables:
Global Module Index quick access to all modules
General Index all functions, classes, terms
Glossary the most important terms explained
Search page search this documentation
Complete Table of Contents lists all sections and subsections
Meta information:
Reporting bugs
About the documentation
History and License of Python
Copyright
> back
index
modules
Python
Documentation
Python 3.7.4 documentation
Welcome! This is the documentation for Python 3.7.4.
Parts of the documentation:
What's new in Python 3.7? or all "What's new" documents since 2.0
Tutorial start here
Library Reference keep this under your pillow
Language Reference describes syntax and language elements
Python Setup and Usage how to use Python on different platforms
Python HOWTOs in-depth documents on specific topics
Installing Python Modules installing from the Python Package Index & other sources
Distributing Python Modules publishing modules for installation by others
Extending and Embedding tutorial for C/C++ programmers
Python/C API reference for C/C++ programmers
FAQs frequently asked questions (with answers!)
Indices and tables:
Global Module Index quick access to all modules
General Index all functions, classes, terms
Glossary the most important terms explained
Search page search this documentation
Complete Table of Contents lists all sections and subsections
Meta information:
Reporting bugs
About the documentation
History and License of Python
Copyright
> back
> exit
```
