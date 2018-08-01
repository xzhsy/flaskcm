"""
Package for the models.
"""

from os import path
import json

class PollNotFound(Exception):
    """Exception raised when a poll/choice object couldn't be retrieved from
    the repository."""
    pass

def _load_samples_json():
    """Loads polls from samples.json file."""
    samples_path = path.join(path.dirname(__file__), 'samples.json')
    with open(samples_path, 'r') as samples_file:
        return json.load(samples_file)
      

      
