import re


def arithmetic_arranger(problems, solve=False):
    width = 0
    top_line = ''
    mid_line = ''
    line = ''
    ans_line = ''
    tab = '    '
    arranged_problems = ''

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for idx, problem in enumerate(problems):
        n = problem.split(' ')
        if len(n) == 3:
            if n[1] == '+' or n[1] == '-':
                if len(n[0]) < 5 and len(n[2]) < 5:
                    if re.match(r'[0-9]{,4}[a-zA-Z]+', n[0]) or re.match(
                            r'[0-9]{,4}[a-zA-Z]+', n[2]):
                        return "Error: Numbers must only contain digits."
                    else:
                        ans = 0
                        width = max(len(n[0]), len(n[2])) + 2
                        top_line += n[0].rjust(width)
                        mid_line += n[1] + n[2].rjust(width - 1)
                        line += '-' * width
                        if solve:
                            if n[1] == '+':
                                ans = int(n[0]) + int(n[2])
                            else:
                                ans = int(n[0]) - int(n[2])
                            ans_line += str(ans).rjust(width)

                        if idx < len(problems) - 1:
                            top_line += tab
                            mid_line += tab
                            line += tab
                            ans_line += tab
                else:
                    return "Error: Numbers cannot be more than four digits."

            else:
                return "Error: Operator must be \'+\' or \'-\'."

    if solve == True: 
        arranged_problems = (top_line + "\n" + mid_line + "\n" + line + "\n" + ans_line)
    else: 
        arranged_problems = (top_line + "\n" + mid_line + "\n" + line)

    return arranged_problems
