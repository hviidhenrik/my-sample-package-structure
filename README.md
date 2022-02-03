Sample Module Repository
========================

## Not for data science projects

For data science projects where you train models, run experiments, that sort of thing, I recommend you use the
cookiecutter package instead:
https://drivendata.github.io/cookiecutter-data-science/#starting-a-new-project

## Python package project structure

If you're not doing a data science project, but just want a quick and dirty file structure for packaging your code as a
Python package, this minimalistic template structure might be useful to you.

### Usage

1. Create a new repo on Github using this as a template.
2. Clone your new repo locally.
3. Change the name of the 'packagename' directory to match your project.*
   Also change this name in the import in packagename/config/\_\_init__.py and in setup.py
4. Write your code!

*This directory is sometimes called simply `src`, but this could cause problems if you have other custom-built packages
as this directory will house your source code and thus be used in imports in other projects.

##### Note:

The template comes predefined with some helpful path definitions. See them in: `packagename/config/definitions.py`

