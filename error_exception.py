def character_frequency(filename):
  """Counts the frequency of each character in the given file."""
  # First try to open the file
  try:
    f = open(filename)
  except OSError:
    
    return None

  # Now process the file
  characters = {}
  for line in f:
    for cha in line:
      characters[cha] = characters.get(cha, 0) + 1
  f.close() 
  return characters
