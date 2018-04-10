import string
alphabet = string.ascii_lowercase;

def extract(query):
  global db
  db = []
  
  def extractlastword(word):
    index = alphabet.find(word[-1])
    if(index != 25):
      new = word[:-1] + alphabet[index+1]
      global db
      db += query(new)
      return extractlastword(new)
    else:
      return False
    
  for letter in alphabet:
    current = query(letter)
    if(len(current) >0):
      lastword = current[-1]
      db += current
      if(len(current)==5):
        isFirstIt = True
        while(len(lastword)>1):
          if(isFirstIt):
            lastwordquery = query(lastword)
            db += lastwordquery[1:]
            isFirstIt = False
          extractlastword(lastword)
          lastword = lastword[:-1]
           
      
  return db
 
    

def main():
    """Runs your solution -- no need to update (except to maybe try out different databases)."""
    # Sample implementation of the autocomplete API
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database

main()