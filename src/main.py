"""
This file exposes instances of all stragies for external usage
"""

from src.config import Config
from src.strategies.google_strategy import GoogleStrategy


gooleStrategy = GoogleStrategy(Config.googleConfig)
