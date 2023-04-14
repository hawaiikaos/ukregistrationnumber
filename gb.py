"""
references:
https://discover.hubpages.com/business/Check-VAT-Numbers-UK
http://sima.cat/nif.php
https://design.tax.service.gov.uk/hmrc-design-patterns/vat-registration-number/
https://library.croneri.co.uk/cch_uk/trto/18-340
"""
from random import randint, choice
import math

def generate_random_number(n):
    """
    generate random number of length n
    """
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
    
def generate_multiplier(n):
    """
    generates a list of descending numbers from length n
    """
    multiplier_list = []
    list_length = int(math.log10(n))+1
    for x in range(list_length):
        multiplier_list.append(list_length - x + 1)
    
    return multiplier_list

def mod97(n):
    """
    This method was used on VAT numbers created prior to 2010
    """
    digits = [int(x) for x in str(n)]
    mdigits = generate_multiplier(n)
    mod97_list = []
    for index, y in enumerate(digits):
        mod97_list.append(digits[index] * mdigits[index])
    
    checksum = sum(mod97_list)
    
    while checksum > 0:
        checksum = checksum - 97
        
    checksum = abs(checksum)
    if checksum < 10:
        checksum = str(0) + str(checksum)
    else:
        checksum = str(checksum)
    
    return checksum

def mod9755(n):
    """
    This method was used from 2010 as HMRC had run out of VAT numbers
    """
    digits = [int(x) for x in str(n)]
    mdigits = generate_multiplier(n)
    mod97_list = []
    for index, y in enumerate(digits):
        mod97_list.append(digits[index] * mdigits[index])
    
    checksum = sum(mod97_list) + 55
    
    while checksum > 0:
        checksum = checksum - 97
        
    checksum = abs(checksum)
    if checksum < 10:
        checksum = str(0) + str(checksum)
    else:
        checksum = str(checksum)
    
    return checksum

def generate_standard_gb_vat():
    prefixes = ["GB", "XI"]
    number_string = generate_random_number(7)

    checksum97 = mod97(number_string)
    final_number97 = str(number_string) + checksum97
    vat_number97 = choice(prefixes) + final_number97
    print("random mod97 VAT number: ")
    print(vat_number97)
    
    checksum9755 = mod9755(number_string)
    final_number9755 = str(number_string) + checksum9755
    vat_number9755 = choice(prefixes) + final_number9755
    
    print("random mod9755 VAT number: ")
    print(vat_number9755)

generate_standard_gb_vat()