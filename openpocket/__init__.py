"""
OpenPocket
Short description
"""

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

__documentation_web__ = 'https://www.uibcdf.org/OpenPocket'
__github_web__ = 'https://github.com/uibcdf/OpenPocket'
__github_issues_web__ = __github_web__ + '/issues'

from . import alpha_spheres
from .get_pockets import get_pockets, show_pockets

