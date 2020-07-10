"""backend module exports krypton backend app callable."""

from .main import app
from .models.interfaces.krypton_model import KryptonModel

__all__  = ['app', 'KryptonModel']
