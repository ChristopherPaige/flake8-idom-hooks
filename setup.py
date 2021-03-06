import os
import setuptools

# the name of the project
name = "flake8_idom_hooks"

# basic paths used to gather files
here = os.path.abspath(os.path.dirname(__file__))
root = os.path.join(here, name)


# -----------------------------------------------------------------------------
# Package Definition
# -----------------------------------------------------------------------------


package = {
    "name": name,
    "py_modules": ["flake8_idom_hooks"],
    "entry_points": {"flake8.extension": ["IDML = flake8_idom_hooks:Plugin"]},
    "python_requires": ">=3.6",
    "description": "Flake8 plugin to enforce the rules of hooks for IDOM",
    "author": "Ryan Morshead",
    "author_email": "ryan.morshead@gmail.com",
    "url": "https://github.com/idom-team/flake8-idom-hooks",
    "license": "MIT",
    "platforms": "Linux, Mac OS X, Windows",
    "classifiers": [
        "Topic :: Software Development :: Libraries :: IDOM :: Quality Assurance",
    ],
    "setup_requires": ["setuptools_scm"],
    "use_scm_version": True,
}


# -----------------------------------------------------------------------------
# Requirements
# -----------------------------------------------------------------------------


requirements = []
with open(os.path.join(here, "requirements", "prod.txt"), "r") as f:
    for line in map(str.strip, f):
        if not line.startswith("#"):
            requirements.append(line)
package["install_requires"] = requirements


# -----------------------------------------------------------------------------
# Library Description
# -----------------------------------------------------------------------------


with open(os.path.join(here, "README.md")) as f:
    long_description = f.read()

package["long_description"] = long_description
package["long_description_content_type"] = "text/markdown"


# -----------------------------------------------------------------------------
# Install It
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    setuptools.setup(**package)
