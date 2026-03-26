class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        output = []
        for i in words:
            temp = True
            if i[0].lower() in first_row:
                for j in range(1, len(i)):
                    if i[j].lower() not in first_row:
                        temp = False
                        break
            if i[0].lower() in second_row:
                for j in range(1, len(i)):
                    if i[j].lower() not in second_row:
                        temp = False
                        break
            if i[0].lower() in third_row:
                for j in range(1, len(i)):
                    if i[j].lower() not in third_row:
                        temp = False
                        break
            if temp == False:
                continue
            output.append(i)
        return output

                            