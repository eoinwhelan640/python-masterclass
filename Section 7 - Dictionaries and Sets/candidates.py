required_skills = ['python','github','linux']

candidates = {
    'anna': {'java','linux','windows','github','python','full stack'},
    'bob': {'github','linux','python'},
    'carol':{'linux','javascript','html','python','github'},
    'daniel':{'pascal','java','c++','github'},
    'ekani':{'html','css','github','python','linux'},
    'fenna':{'linux','pascal','java','c','lisp','modula-2','perl','github'},
}

interviewees = set()
# for candidate, skills in candidates.items():
#     if skills.issuperset(required_skills):
#         interviewees.add(candidate)

#or doing the other way
# for candidate, skills in candidates.items():
#     if set(required_skills).issubset(skills):
#         interviewees.add(candidate)

# Use a "proper" superset to rule out peopkle with excat matches, we want desired skills + others
for candidate, skills in candidates.items():
    # Youd wanna initialise required skills as a set not within the loop
    if skills > set(required_skills):
        interviewees.add(candidate)
print(interviewees)

