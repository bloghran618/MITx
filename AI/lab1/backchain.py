from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
#     result = [hypothesis]
#     for rule in rules:
#         for expr in rule.consequent():
#             if (match(expr, hypothesis) or expr) == hypothesis:
#                 if isinstance(rule.antecedent(), str):
#                     result.append(backchain_to_goal_tree(rules, populate(rule.antecedent(), match(expr, hypothesis))))
#                     result.append(populate(rule.antecedent(), match(expr, hypothesis)))
#                 else:
#                     entries = [populate(itera, match(expr, hypothesis)) for itera in rule.antecedent()]
#                     new_res = []
#                     for entry in entries:
#                         new_res.append(backchain_to_goal_tree(rules, entry))
#                     result.append(create_statement(new_res, rule.antecedent()))
#     return simplify(OR(result))
#
# def create_statement(entries, rule):
#     if isinstance(rule, AND):
#         return AND(entries)
#     if isinstance(rule, OR):
#         return OR(entries)

    results = [hypothesis]
    for rule in rules:
        for expr in rule.consequent():
            if match(expr, hypothesis) or expr == hypothesis:
                if isinstance(rule.antecedent(), str):
                    results.append(backchain_to_goal_tree(rules, populate(rule.antecedent(), match(expr, hypothesis))))
                    results.append(populate(rule.antecedent(), match(expr, hypothesis)))
                else:
                    statements = [populate(ante_expr, match(expr, hypothesis)) for ante_expr in rule.antecedent()]
                    new_results = []
                    for statement in statements:
                        new_results.append(backchain_to_goal_tree(rules, statement))
                    results.append(create_statement(new_results, rule.antecedent()))
    return simplify(OR(results))


def create_statement(statements, rule):
    if isinstance(rule, AND):
        return AND(statements)
    elif isinstance(rule, OR):
        return OR(statements)

# Here's an example of running the backward chainer - uncomment
# it to see it work:
print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')
