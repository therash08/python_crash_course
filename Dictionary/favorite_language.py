# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'jami': 'java',
#     'ashh': 'javascript',
# }


# # print(favorite_language)
# print("sara favorite language is " + favorite_language['ashh'].title())


# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'jami': 'java',
#     'ashh': 'javascript',
# }

# for name, language in favorite_language.items():
#     print(name.title() + 's favorite language is ' + language.title())


# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'jami': 'java',
#     'ashh': 'javascript',
# }
# for name in favorite_language.values():
#     print(name.title())

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("erin, please take our poll!")
