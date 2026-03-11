import pytest

def fix_phone_num(phone_num_to_fix):
  for char in "-() ":
    phone_num_to_fix = phone_num_to_fix.replace(char, "")
  
  if not phone_num_to_fix.isdigit():
    raise ValueError("Phone number contains non-numeric characters.")
  
  if len(phone_num_to_fix) != 10:
    raise ValueError("Phone number must be exactly 10 digits.")
  
  area_code = phone_num_to_fix[0:3]
  three_part = phone_num_to_fix[3:6]
  four_part = phone_num_to_fix[6:]
  
  return f"({area_code}) {three_part} {four_part}"

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5554429876") == '(555) 442 9876'
  assert fix_phone_num("3216543333") == '(321) 654 3333'

def test_fix_phone_num_formatting():
  assert fix_phone_num("555-442-9876") == '(555) 442 9876'
  assert fix_phone_num("(321) 654 3333") == '(321) 654 3333'

def test_fix_phone_num_non_digits():
  with pytest.raises(ValueError):
    fix_phone_num("334dfdee45")
  with pytest.raises(ValueError):
    fix_phone_num("abcdefghij")
