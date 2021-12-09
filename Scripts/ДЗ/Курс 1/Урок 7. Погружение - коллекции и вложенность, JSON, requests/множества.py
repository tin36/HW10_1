my_skills = set(['python', 'flask', 'django', 'критическое мышление', 'планирвоание', 'переговоры', 'css', 'html'])

backend_skills = {'linux', 'terminal', 'python', 'flask', 'django', 'restapi'}
frontend_skills = {'html', 'css', 'javascript'}
soft_skills = {'презентация', 'планирование', 'переговороы', 'лидерство', 'критическое мышление'}

print(frontend_skills.difference(my_skills))
print(my_skills.intersection(backend_skills))
print(my_skills.difference(backend_skills.union(frontend_skills)))
print(soft_skills.issubset(my_skills))
print(backend_skills.union(frontend_skills))