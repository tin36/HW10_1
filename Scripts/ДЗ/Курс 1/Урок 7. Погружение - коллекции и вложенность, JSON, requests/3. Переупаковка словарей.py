coder_info = {
    "name": "Алексей",
    "languages": {
        "java": "beginner",
        "php": "middle",
        "python": "senior",
        "go": "none",
    }
}


languages = []
for lang, level in coder_info['languages'].items():
  if level in ('middle', 'senior'):
    languages.append(lang)

coder_info_short = {"name": coder_info['name'], "languages": languages}

print(coder_info_short)