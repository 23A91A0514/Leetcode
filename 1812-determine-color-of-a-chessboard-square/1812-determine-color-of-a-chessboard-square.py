class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a = coordinates[0]
        b = coordinates[1]
        
        if ord(a) % 2 == 1 and int(b) % 2 == 1:
            return False
        elif ord(a) % 2 == 1 and int(b) % 2 == 0:
            return True
        elif ord(a) % 2 == 0 and int(b) % 2 == 1:
            return True
        else:
            return False