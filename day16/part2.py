import sys
import pytest


def solve(
    input_s, name_contains="departure"
):  # pylint: disable=too-many-locals,too-many-statements,too-many-branches
    rules = {}

    rules_s, your_ticket_s, tickets_s = input_s.split("\n\n")
    for line in rules_s.splitlines():
        name, rule = line.split(": ", 1)
        r1, r2 = rule.split(" or ")
        rules[name] = (
            tuple(int(i) for i in r1.split("-")),
            tuple(int(i) for i in r2.split("-")),
        )

    your_ticket = tuple(
        int(i) for i in your_ticket_s.replace("your ticket:\n", "").split(",")
    )

    valid_tickets = []
    for line in tickets_s.replace("nearby tickets:\n", "").splitlines():
        check = {}
        ticket = tuple(int(i) for i in line.split(","))
        for num in ticket:
            check[num] = 0
            for rule in rules.values():
                if rule[0][0] <= num <= rule[0][1] or rule[1][0] <= num <= rule[1][1]:
                    check[num] += 1
        if not tuple(k for k, v in check.items() if v == 0):
            valid_tickets.append(ticket)
    positions = {}
    index = 0
    vacant_rules = set(rules)
    uncertain = {}
    while index < len(rules):
        index_rules = set()
        for ticket in valid_tickets:
            ticket_rules = set()
            num = ticket[index]
            for name in vacant_rules:
                rule = rules[name]
                if rule[0][0] <= num <= rule[0][1] or rule[1][0] <= num <= rule[1][1]:
                    ticket_rules.add(name)
            if len(ticket_rules) == 1:
                frule = list(ticket_rules)[0]
                vacant_rules.remove(frule)
                positions[index] = list(ticket_rules)[0]
                break

            if not index_rules:
                index_rules = ticket_rules
            else:
                index_rules &= ticket_rules
            if len(index_rules) == 1:
                frule = list(index_rules)[0]
                vacant_rules.remove(frule)
                positions[index] = frule
                break
        else:
            uncertain[index] = index_rules
        new_uncertain = {}
        for k, v in uncertain.items():
            for rule in positions.values():
                if rule in v:
                    v.remove(rule)
            if len(v) == 1:
                positions[k] = list(v)[0]
            else:
                new_uncertain[k] = v
        uncertain = new_uncertain
        index += 1

    while uncertain:
        new_uncertain = {}
        for k, v in uncertain.items():
            for rule in positions.values():
                if rule in v:
                    v.remove(rule)
            if len(v) == 1:
                positions[k] = list(v)[0]
            else:
                new_uncertain[k] = v
        uncertain = new_uncertain

    res = []
    for k, v in positions.items():
        if name_contains in v:
            res.append(your_ticket[k])
    answer = 1
    for r in res:
        answer *= r
    return answer


INPUT_S = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""


INPUT_S2 = """\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""


@pytest.mark.parametrize(
    ("input_s", "name_contains", "expected"),
    ((INPUT_S, "class", 1), (INPUT_S2, "class", 12)),
)
def test(input_s, name_contains, expected):
    assert solve(input_s, name_contains) == expected


def main():
    with open("input.txt") as f:
        print(solve(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
