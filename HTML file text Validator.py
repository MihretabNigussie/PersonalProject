from MyStack import Stack


class Validator:
    def XMLReader(self, filePath):
        file = open(filePath)
        fileInString = file.read()
        return fileInString

    def validator(self, file):
        stack_1 = Stack()
        list_created = file.split("\n")
        print(list_created)
        line_no = 0
        finder_1 = list_created[line_no].find("<")
        message = "No Error"

        while finder_1 == -1 and len(list_created) - 1 > line_no:
            line_no += 1
            finder_1 = list_created[line_no].find("<")

        while finder_1 != -1:
            finder_2 = list_created[line_no].find(">", finder_1 + 1)

            space = list_created[line_no][finder_1 +1:finder_2].find(" ")
            if space == -1:
                tag = list_created[line_no][finder_1+1:finder_2]
            else:
                tag = list_created[line_no][finder_1+1:space+1]

            if not tag.startswith("/") and not tag.endswith("/"):
                # if they are neither end_tags nor empty_elements
                stack_1.push(tag)
            elif not tag.endswith("/"):
                # if the tag is not an empty_element
                if stack_1.isEmpty():
                    output = "Line: {:}\nTag: {:}".format(line_no + 1, tag)
                    return output
                if tag[1:] != stack_1.pop():
                    output = "Line: {:}\nTag: {:}".format(line_no + 1, tag)
                    return output
            else:
                message = "There is empty element"

            finder_1 = list_created[line_no].find("<", finder_2 + 1)

            while finder_1 == -1 and len(list_created) - 1 > line_no:
                line_no += 1
                finder_1 = list_created[line_no].find("<")

        if not stack_1.isEmpty():
            output = "Line: {:}\nTag: {:} should be closed".format(line_no + 1, s.pop())
            return output
        return message


valid = Validator()
filePath = "valid.txt"
file = valid.XMLReader(filePath)
print(valid.validator(file))
