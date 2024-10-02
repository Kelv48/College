'''def meanBoutsPerPatient ():
    inFile = open ("InflammatoryIBS.txt.csv", "r")

    for patient in inFile:
        patient = patient.strip("\n")
        patient_data = patient.split(",")

        total_bouts = 0
        for data_point in patient_data:
            data_point = int(data_point)
            total_bouts += data_point
        average = total_bouts / len(patient_data)

        print("The average is", average)

    inFile.close()

meanBoutsPerPatient()'''

def meanBoutsPerPatient ():
    inFile = open ("InflammatoryIBS.txt.csv", "r")
    
    total_bouts = 0
    total_records = 0
    for patient in inFile:
        patient = patient.strip("\n")
        patient_data = patient.split(",")
   
        for data_point in patient_data:
            data_point = int(data_point)
            total_bouts += data_point
        total_records += len(patient_data)
    average = total_bouts / total_records

    print("The average is", average)

    inFile.close()

meanBoutsPerPatient()

















