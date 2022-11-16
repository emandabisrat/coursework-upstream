"""
CMSC 14100 Project Aut 22
"""

from library import Library, LibraryException
from version import Version

class LibraryHub:
    """
    A class for a registry managing libraries.
    """
    def __init__(self):
        """
        Create a new LibraryHub instance.
        """
        self.library_dict = {}
        
        


    def register_new_library(self,
                             name,  # Name of the library
                             version,  # Version number
                             is_testing = False,  # Is not ready to be used.
                             ):
        """
        Creates a new Library and registers it with the LibraryHub for later
        lookup/use. Should raise a LibraryException is the Library version is 
        not exact (e.g. could match to more than one version stored) OR if the 
        exact Library already exists.

        Inputs:  
            name (str): The library name. Case sensitive  
            version(str): The exact library version number  
            is_testing(bool): If the library is not ready for use  

        Returns(Library): The newly created Library object
        """
        new_library = Library(name,version,is_testing)
        if new_library.name in self.library_dict:
            lib = self.library_dict[name]
        else:
            self.library_dict[name] = [new_library]
        return new_library
            

    def find_latest_version(self, name, include_testing = False):
        """
        Find the latest version of a library name.  Should raise a
        LibraryException is the Library name cannot be found

        Inputs:  
            name(str): The name of the library  
            include_testing(bool): Consider testing libraries  

        Returns (Library): The largest version for a library name
        """
        if name in self.library_dict:
            if not include_testing:
                non_testing = lib for lib in self.library_dict[name] if not lib.is_testing
                if len(non_testing) > 0:
                    return non_testing[-1]
                else:
                    raise LibraryException
        else:
            raise LibraryException

    def get_library(self, name, version_requirement):
        """
        Find a registered Library object by the name and version.
        If more than one registered version satisfies the version requirement,
        return the Library with the highest version number that satisfies the
        requirement and is not in testing.
        If only one registered version satisfies the requirment, return the
        library regardless if in testing or not. If version_requirement is
        exact, then only an exact match should be found.

        Inputs:  
          name (str): The library name to match. Case sensitive  
          version_requirement(str): The library version requirement  

        Returns (Library | None): The Library that satisfies the
        version_requirement. If more than one are registered, then the
        largest/highest one that is not testing should be returned.
        None is returned if no valid library can be found.
        """
        