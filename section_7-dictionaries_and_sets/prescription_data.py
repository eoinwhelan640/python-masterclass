# drugs
amlodipine = ("amlodipine", "Blood pressure")
buspirone = ("buspirone", "Anxiety disorders")
carbimazole = ("carbimazole", "Antithyroid agent")
citalopram = ("citalopram", "Antidepressant")
edoxaban = ("edoxaban", "anti-coagulant")
erythromycin = ("erythromycin", "Antibiotic")
lusinopril = ("lusinopril", "High blood pressure")
metformin = ("metformin", "Type 2 diabetes")
methotrexate = ("methotrexate", "Rheumatoid arthritis")
paracetamol = ("paracetamol", "Painkiller")
propranol = ("propranol", "Beta blocker")
simvastatin = ("simvastatin", "High cholesterol")
warfarin = ("warfarin", "anti-coagulant")

# Drugs that shouldn't be taken together
adverse_interactions = [
    {metformin, amlodipine},
    {simvastatin, erythromycin},
    {citalopram, buspirone},
    {warfarin, citalopram},
    {warfarin, edoxaban},
    {warfarin, erythromycin},
    {warfarin, amlodipine},
]

# print("PRINTING TOP LEVEL ONLY")
# for a in adverse_interactions:
#     print(f"A is {a}")
#     print()
#
# print("PRINTING SECOND LEVEL ONLY")
#
# for a,b in adverse_interactions:
#     print(f"A is {a}")
#     print(f"B is {b}")
#     print()
#
#
# print("PRINTING THIRD LEVEL ONLY")
# for (a,b),(c,d) in adverse_interactions:
#     print(f"A is {a}")
#     print(f"B is {b}")
#     print(f"C is {c}")
#     print(f"D is {d}")
#     print()

for a,(b,c) in adverse_interactions:
    print(f"first thing is: {a}")
    print(f"Second level gives me: {b} & {c}")

# Patient prescriptions
patients = {
    "Anne": {methotrexate, paracetamol},
    "Bob": {carbimazole, erythromycin, methotrexate, paracetamol},
    "Charley": {buspirone, lusinopril, metformin},
    "Denise": {amlodipine, lusinopril, metformin, warfarin},
    "Eddie": {amlodipine, propranol, simvastatin, warfarin},
    "Frank": {buspirone, citalopram, propranol, warfarin},
    "Georgia": {carbimazole, edoxaban, warfarin},
    "Helmut": {erythromycin, paracetamol, propranol, simvastatin},
    "Izabella": {amlodipine, citalopram, simvastatin, warfarin},
    "John": {simvastatin},
    "Kenny": {amlodipine, citalopram, metformin},
}


t = [
    {('X','Y'),("Z","K")},
    {(1,2),(3,4)},
    {("M","N"),("i","j")},
]

print("PRINTING a ONLY")
for a in t:
    print(f"A is {a}")
    print()

print("PRINTING a,b ONLY")

for a,b in t:
    print(f"A is {a}")
    print(f"B is {b}")
    print()


print("PRINTING a,(b,c) ONLY")

for a,(b,c) in t:
    print(f"A is {a}")
    print(f"B is {b}")
    print(f"C is {c}")
    print()

print("PRINTING (a,b),(c,d) ONLY")
for (a,b),(c,d) in t:
    print(f"A is {a}")
    print(f"B is {b}")
    print(f"C is {c}")
    print(f"D is {d}")
    print()
