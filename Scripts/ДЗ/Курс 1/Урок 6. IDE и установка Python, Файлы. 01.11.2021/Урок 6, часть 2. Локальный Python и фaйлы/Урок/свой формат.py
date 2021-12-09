with open('st.txt') as file:
    for st_data in file:
        # data = st_data.rstrip('\n').split(":")
        # name = data[0]
        # language = data[1]
        name, language = st_data.rstrip('\n').split(":")
        print(f'{name} учит язык {language}!')

