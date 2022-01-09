#!/usr/bin/env python
import re
import datetime
now = datetime.datetime.now()

def isNationalId(id):
    """ Validating National ID
    >>> isNationalId("1199672222000040"); # 
    True
    >>> isNationalId("1201772222000040"); # 
    False

    """
    ID_LENGTH=16
    minAge = 16
    pattern = r'^[1-3](19|20)\d{2}[7-8]\d{7}[0-9]\d{2}$'
    regex = re.compile(pattern)
    try:
        if (len(id) < ID_LENGTH):
            return False
        if (len(id) > ID_LENGTH):
            return False
        if(now.year - int(id[1:5]) < minAge):
            return False
        match = regex.search(id)
        if not match:
            return False
        return True 
    except TypeError:
        return "Input should be string"

def isPhoneNumber(number):
    """ Validating Phone Numbers
    >>> isPhoneNumber("0788854444"); 
    True
    >>> isPhoneNumber("0778854444"); 
    False
    """
    pattern = r'^(\+?25)?(079|078|075|073|072)\d{7}$'
    regex = re.compile(pattern)
    match = regex.search(number)
    if not match:
        return False;
    return True
def isTinNumber(number):
    """Validating TIN number

    >>> isTinNumber("107610474"); #
    True
    >>> isTinNumber("1000043485"); # 
    False
    """

    pattern = r'^(1|0)\d{8}$'
    regex = re.compile(pattern)
    match = regex.search(number)
    if not match:
        return False;
    return True

def isNewAddress(address, kigaliOnly=True):
    """ 
        Currently only supports Kigali Roads. 


        >>> isNewAddress("KK 30 rd 8")
        True
        >>> isNewAddress("KT 30 rd 8")
        False
        >>> isNewAddress("KN 30 FN 8")
        False
    """
    # validate street address
    # pattern=PRONVINCE_IN+DISTRICT_IN NUMBER (ST or AVE)

    Provinces=["Kigali","South","North","East","West"]
    ProvincesInitials=[x[0] for x in Provinces]
    Districts={"S":["Gisagara","Huye","Kamonyi","Muhanga","Nyamagabe","Nyanza","Nyaruguru","Ruhango"],
                "K":["Gasabo","Kicukiro","Nyarugenge"],
                "E":["Bugesera","Gatsibo","Kayonza","Kirehe","Ngoma","Nyagatare","Rwamagana"],
                "W":["Karongi","Ngororero","Nyabihu","Nyamasheke", "Rubavu","Rusizi","Rutsiro"],
                "N":["Burera","Gakenke","Gicumbi","Musanze","Rulindo"]}

    address=address.upper()
    address= re.sub(r"[\n\t\s,;:]*", "", address)
    if kigaliOnly:
        pattern=r'^(KN|KK|KN)( )*[0-9]{0,4}( )*(AVE|ST|RD)[0-9]*$'  # Support Kigali
    else:
        pattern=r'^(S|K|E|W|N)[A-Z]{1,3}( )*[0-9]{0,4}( )*(AVE|ST|RD)[0-9]*$' # partially suppport other addres 


    regex=re.compile(pattern)
    match=regex.match(address)
    if not match:
        return False
    else:
        return True
if __name__ == "__main__":
    import doctest
    doctest.testmod()