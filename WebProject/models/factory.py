"""
Factory for the different types of repositories.
"""
from  WebProject.models.DBRepository import Repository

def create_repository(settings):
    """Creates a repository from its name and settings. The settings
    is a dictionary where the keys are different for every type of repository.
    See each repository for details on the required settings."""
 

    return Repository(settings)

