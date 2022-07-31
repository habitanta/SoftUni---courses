


def shell_fill_with_electrons(electrons):
    shells = []
    shell_number = 0
    while electrons > 0:
        shell_number += 1
        shell_capacity = 2 * (shell_number ** 2)
        if shell_capacity > electrons:
            shells.append(electrons)
            electrons = 0
            break
        else:
            shells.append(shell_capacity)
            electrons -= shell_capacity
    return shells



all_electrons = int(input())
result = shell_fill_with_electrons(all_electrons)
print(result)