"""
CMSC 14100 Project Aut 22
"""
from version import Version


class LibraryException(Exception):
    """
    A simple exception for described error conditions. You should not
    modify this Class at all.
    """
    pass


class Library:
    """
    A class to represent a published library. This will have:  
        - A name  
        - An exact version (major, minor, and patch)  
        - is_testing flag/attribute which indicates this library is "not ready"
    """
    def __init__(self,
                 name,  # Name of the library
                 version,  # Version number
                 is_testing = False,  # Library is in testing
                 ):
        """
        Create a new library. Raise a LibraryException if the version is not 
        exact.

        Inputs:  
            name(str): The name of the library  
            version(str): The semantic version number  
            is_testing(bool): If the library is for testing only  
        """
        self.name = name 
        self.version = version
        self.is_testing = is_testing
        
        x = self.version.split('.')

        if len(x) < 3 or x[2] == '': 
            raise LibraryException("Version not exact")
        

  
    def compare_version(self, other):
        """
        Check if this version is smaller, the same, or greater than the
        other version. Throws a Library Exception if the names are not the same.

        Inputs:  
            other (Library): a Library to compare against

        Returns (int):  
          -1 if self is smaller than other,  
          0 if they have the same version number,  
          1 if self is larger than other
        """
        assert isinstance(other, Library)

        self_version = Version(self.version)
        other_version = Version(other.version)
        
        if self.name != other.name: 
            raise LibraryException
        return Version.compare_version(self_version, other_version)  
   
   
    def meets_version_req(self, version_needed):
        """
        Checks if this Library meets the version number requirement.

        Inputs:  
            version_number(str): The required version as a string  

        Returns (bool): If the library meets the requirement
        """
        assert isinstance(version_needed, str)
        return Version(self.version).meets_requirement(Version(version_needed))
