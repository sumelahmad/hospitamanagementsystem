class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def display_details(self):
        print(f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Disease: {self.disease}")

    def update_info(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
        print("Patient information updated successfully.")


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def display_details(self):
        print(f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}")

    def update_info(self, name, specialization):
        self.name = name
        self.specialization = specialization
        print("Doctor information updated successfully.")


class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}

    # Patient Module
    def add_patient(self, patient_id, name, age, disease):
        if patient_id not in self.patients:
            self.patients[patient_id] = Patient(patient_id, name, age, disease)
            print(f"Patient {name} added successfully.")
        else:
            print("Patient ID already exists!")

    def show_all_patients(self):
        if not self.patients:
            print("No patients in the system.")
        else:
            print("Patient List:")
            for patient in self.patients.values():
                patient.display_details()

    def update_patient_info(self, patient_id):
        patient = self.patients.get(patient_id)
        if patient:
            print("Update Patient Information:")
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            disease = input("Enter new disease: ")
            patient.update_info(name, age, disease)
        else:
            print(f"No patient found with ID: {patient_id}")

    # Doctor Module
    def add_doctor(self, doctor_id, name, specialization):
        if doctor_id not in self.doctors:
            self.doctors[doctor_id] = Doctor(doctor_id, name, specialization)
            print(f"Doctor {name} added successfully.")
        else:
            print("Doctor ID already exists!")

    def show_all_doctors(self):
        if not self.doctors:
            print("No doctors in the system.")
        else:
            print("Doctor List:")
            for doctor in self.doctors.values():
                doctor.display_details()

    def update_doctor_info(self, doctor_id):
        doctor = self.doctors.get(doctor_id)
        if doctor:
            print("Update Doctor Information:")
            name = input("Enter new name: ")
            specialization = input("Enter new specialization: ")
            doctor.update_info(name, specialization)
        else:
            print(f"No doctor found with ID: {doctor_id}")


def main():
    system = HospitalManagementSystem()

    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Add Doctor")
        print("4. View All Doctors")
        print("5. Update Patient Information")
        print("6. Update Doctor Information")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            pid = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = int(input("Enter Patient Age: "))
            disease = input("Enter Patient Disease: ")
            system.add_patient(pid, name, age, disease)

        elif choice == '2':
            system.show_all_patients()

        elif choice == '3':
            did = input("Enter Doctor ID: ")
            name = input("Enter Doctor Name: ")
            specialization = input("Enter Specialization: ")
            system.add_doctor(did, name, specialization)

        elif choice == '4':
            system.show_all_doctors()

        elif choice == '5':
            pid = input("Enter Patient ID to update information: ")
            system.update_patient_info(pid)

        elif choice == '6':
            did = input("Enter Doctor ID to update information: ")
            system.update_doctor_info(did)

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
