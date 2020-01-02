"""
Write a function isIntArray or is_int_array with the below signature.

def is_int_array(arr):
    return True

  * returns *True* if every element in an array is an integer or a float with no decimals.
  * returns *True* if array is empty.
  * returns *False* for every other input.

"""


def is_int_array(arr):
    if not isinstance(arr, list):
        return False
    try:
        for e in arr:
            if int(e) != e:
                return False
    except:
        return False
    return True
