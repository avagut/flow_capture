"""Navigation Structures for site."""
from flask import Blueprint

bl_nav = Blueprint('navigation',
                   __name__,
                   template_folder='templates',
                   static_folder='static'
                   )

from . import views  # noqa