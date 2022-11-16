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
        split_v = version_str.strip(".").split(".")
        v_length = len(split_v)
        assert v_length <= 3 and v_length >= 1
        v_nums = [int(v) for v in split_v]
        self.major = v_nums[0] 
        self.minor = v_nums[1] if v_length >= 2 else -1
        self.patch = v_nums[2] if v_length == 3 else -1
        
        
       
       
    

    def compare_num(self,version1,version2):
        if version1 < version2:
            return -1
        if version1 == version2:
            return 0
        if version1 > version2:
            return 1

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
        result = 0
        comparisons = [
            self.compare_num(self.major,other.major), 
            self.compare_num(self.minor,other.minor),
            self.compare_num(self.patch,other.patch)
        ] 
        for i in comparisons:
            if i != result:
                return i 
        return result


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
        assert isinstance(req,Version)
        return self.compare_version(req) >= 0


