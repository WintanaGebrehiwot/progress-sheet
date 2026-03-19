class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read = 0
        write = 0

        while read < len(chars):
            current_char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1

            chars[write] = current_char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
        

        