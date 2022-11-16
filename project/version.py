"""
CMSC 14100 Project Aut 22
"""

class Version:
    """
    A class to represent a semantic version which includes a:  
        - major version number  
        - an optional minor number  
        - an optional patch number  

    A published library will have an exact version with major, minor, and patch
    values, such as 1.0.3 where 1 is the major, 0 is the minor, and 3 is the
    patch. A version used for searching or library matching could be partial,
    such as 1, 1., 2.1 or 2.1.
    """
    def __init__(self, version_str):
        """
        Create a new Version instance based on a version string in the form of
        X, X., X.Y, X.Y., or X.Y.Z where X,Y,and Z are natural numbers.

        Inputs:
            version_str(str): The given semantic version number
        """
        new_version = version_str.split('.')
        print(new_version)
        if len(new_version) == 3:
            new_version[0] = self.major
            new_version[1] = self.minor
            new_version[3] = self.patch
        elif len(new_version) == 2:
            new_version[0] = self.major
            new_version[1] = self.minor
            self.patch = '-1'
        elif len(new_version) == 1:
            new_version[0] = self.major
            self.minor = '-1'
            self.patch = '-1'
        
        ### TODO project 1
        ### Add your attributes and initialize them
        pass


    def compare_version(self, other):
        """
        Check if this version is smaller, the same, or greater than the
        other version. If a version is partial assume the missing components
        are the smallest possible value (e.g. < 0).

        Inputs:
            other (Version): a Version to compare against

        Returns (int):  
            -1 if self is smaller than other,  
            0 if they have the same version number,  
            1 if  self is larger than other
        """
        assert isinstance(other, Version)
    


    def meets_requirement(self, req):
        """
        Checks to see if this version satisfies the requirement.
        Req is a version that was initialized with a string like
        X, X., X.Y, X.Y., or X.Y.Z,
        where X is the major number, Y is the minor, and Z is patch.

        For exact requirement versions (X.Y.Z) this Version will evaluate to
        True if the versions are the same.

        For partial requirement versions (e.g. X or X.Y) this Version will
        evaluate to true if the given parts (X and/or Y) are the same.
      
        Inputs:  
            req(Version): The required version

        Output(bool): If this Version satisfies the requirement
        """
    
