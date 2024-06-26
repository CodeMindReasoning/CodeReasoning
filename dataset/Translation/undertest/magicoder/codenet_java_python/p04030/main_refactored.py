class main:
    class FastScanner:
        def __init__(self):
            self.buffer = bytearray(1024)
            self.ptr = 0
            self.buflen = 0
    
        def has_next_byte(self):
            if self.ptr < self.buflen:
                return True
            else:
                self.ptr = 0
                try:
                    self.buflen = self.in.readinto(self.buffer)
                except EOFError:
                    self.buflen = 0
                    return False
                if self.buflen <= 0:
                    return False
            return True
    
        def read_byte(self):
            if self.has_next_byte():
                return self.buffer[self.ptr]
            else:
                return -1