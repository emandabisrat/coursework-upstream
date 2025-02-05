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
        self.split_v = version_str.split('.')
        if self.split_v[-1] == '': 
            self.split_v.pop()
        
        while len(self.split_v) < 3:  
            self.split_v.append(-1)  
        self.major = int(self.split_v[0])
        self.minor = int(self.split_v[1])
        self.patch = int(self.split_v[2])
        
       
       


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
        if self.major < other.major:
            return -1 
        if self.major > other.major: 
            return 1 
        if self.minor < other.minor: 
            return -1 
        if self.minor > other.minor: 
            return 1
        if self.patch < other.patch: 
            return -1 
        if self.patch > other.patch: 
            return 1 
        return 0


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
        assert isinstance(req, Version)
        
        if self.major == req.major: 
            if req.minor == -1:
                return True
            if self.minor == req.minor: 
                if req.patch == -1:
                    return True 
                if self.patch != req.patch: 
                    return False 
            if self.minor != req.minor: 
                return False 
            else: 
                return True 
        return False

