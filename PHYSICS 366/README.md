# Study HPC in Python
Study HPC tools available in Python.


---

# MPI
* <a href="https://mpi4py.readthedocs.io/en/stable/intro.html">mpi4py</a>: Message Passing Interface (MPI) for Python.
  * <a href="https://mpi4py.readthedocs.io/en/stable/tutorial.html">Tutorial</a> in the package documentation.
  * <a href="https://www.eijkhout.net/home/landing-page.html">Victor Eijkhout</a> has written <a href="https://theartofhpc.com/">textbooks</a> on HPC, including the topics on MPI.
    * <a href="https://web.corral.tacc.utexas.edu/CompEdu/pdf/pcse/mpi_course.pdf">A course material</a> on Texas Advanced Computing Center (TACC). It is not much python-friendly, but we can try to solve some example exercises.

---

# Video links
* <a href="https://www.youtube.com/@texasadvancedcomputingcent1015">Texas Advanced Computing Center (TACC)</a> channel has some useful video lectures.
  * <a href="https://youtu.be/R4e4iKoB0t4">Intro to HPC Terms - 1</a>: Some of them may be TACC specific (e.g. 'idev' command)
  * <a href="https://youtu.be/fHo5FXOnLTU">MPI Foundations 3-25-19</a>: Workshop based on <a href="https://web.corral.tacc.utexas.edu/CompEdu/pdf/pcse/mpi_course.pdf">this course material</a> I think. It is not much python-friendly, but we can try to solve some example exercises.

---

# Useful linting and formatting tools
It is nice to follow the PEP 8 Style Guide for Python Code: https://peps.python.org/pep-0008/

Good tools to help this are:
* flake8: A linter. https://flake8.pycqa.org/en/latest/
* Black: A formatter. https://github.com/psf/black; https://black.readthedocs.io/en/stable/index.html

## Using Black
Black (https://github.com/psf/black) is a very convenient tool. A quick way to apply this style guide automatically on the files you have written is as follows.
* Install black: `pip install black`.
    * If you want to format Jupyter Notebooks, install with `pip install "black[jupyter]"`.
* Use on a file or directory:
    *  `black {source_file_or_directory}`
    * `python -m black {source_file_or_directory}`: If the above command doesn't work.
    * Examples: `black test.py`; `black test.ipynb` (if black[jupyter] was also installed)
* To see the difference only without saving the file, use `--diff`
    * Example: `black test.py --diff`

If you use an IDE such as VS Code or other tools, you can configure settings to automatically apply this whenever you save a file. See integrations section of the documents: https://black.readthedocs.io/en/stable/integrations/index.html
