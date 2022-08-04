from prescription_data import *
trial_patients = ['Denise',"Eddie", "Frank", "Georgia","Kenny"]

# Remove Warfarin and add edoxaban
# for patient in trial_patients:
#     patients[patient].remove(warfarin)
#     patients[patient].add(edoxaban)

for patient in trial_patients:
    prescription = patients[patient]
    # if we used discard instead of remove here, we'd try remove warfarin from people who werent taking it
    # And move onto prescribing edoxan in place of it. SO even people not taking warfarin would get edoxaban
    # We would want an error thrown here
    if warfarin in prescription:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    else:
        print(f"Patient {patient} is not taking warfarin. "
              f"Please remove {patient} from the trial")
    print(patient,prescription)









