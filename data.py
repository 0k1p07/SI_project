import null as null


class Subject:
    def __init__(self, name, necessary_classroom_type):
        self.name = name
        self.necessary_classroom_type = necessary_classroom_type

    def toString(self):
        return "Nazwa przedmiotu: " + self.name + "; Konieczny specyficzny typ sali: " + str(
            self.necessary_classroom_type)

    def printName(self):
        print(self.name, end=' ')

class Classroom:
    def __init__(self, number, preferred_subject_list):
        self.number = number
        self.preferred_subject_list = preferred_subject_list

    def toString(self):
        string = ""
        for s in self.preferred_subject_list:
            string += s.toString() + "\n"
        if self.preferred_subject_list == []:
            string += "\n"
        return "Numer sali: " + self.number + "\nLista preferowanych przedmiotów: " + string

    def printNumber(self):
        print(self.number, end=' ')

class Class:
    def __init__(self, name, subject_list):
        self.name = name
        self.subject_list = subject_list

    def toString(self):
        string = ""
        for s in self.subject_list:
            string += s[0].toString() + "\nPrzedmiot rozszerzony: " + str(s[1]) + "\nLiczba godzin: " + str(s[2]) + "\nNauczyciel:\n   " + s[3].toString() + "\n"
        return "Nazwa klasy: " + self.name + "\nLista przedmiotów: " + string

    def printName(self):
        print(self.name, end=' ')

class Teacher:
    def __init__(self, name, subjects_taught_list):
        self.name = name
        self.subjects_taught_list = subjects_taught_list

    def toString(self):
        string = ""
        for s in self.subjects_taught_list:
            string += "\n       " + s.toString()
        return "Imię i nazwisko: " + self.name + "\n   Lista uczonych przedmiotów: " + string + "\n"

    def printName(self):
        print(self.name, end=' ')

def findObject(object_list, name):
    for obj in object_list:
        if obj.name == name:
            return obj
    return null


hours = ["7:10-7:55", "8:00-8:45", "8:55-9:40", "9:50-10:35", "10:55-11:40", "11:50-12:35",
        "12:45-13:30", "13:40-14:25", "14:35-15:20", "15:30-16:15", "16:25-17:10", "17:15-18:00"]

days = ["Mon", "Tue", "Wed", "Thur", "Fri"]

subjects = []
subject = Subject("Polski", False)
subjects.append(subject)
subject = Subject("Angielski", False)
subjects.append(subject)
subject = Subject("Francuski", False)
subjects.append(subject)
subject = Subject("Niemiecki", False)
subjects.append(subject)
subject = Subject("Matematyka", False)
subjects.append(subject)
subject = Subject("Geografia", False)
subjects.append(subject)
subject = Subject("Podstawy przedsiębiorczości", False)
subjects.append(subject)
subject = Subject("Historia", False)
subjects.append(subject)
subject = Subject("WOS", False)
subjects.append(subject)
subject = Subject("Biologia", False)
subjects.append(subject)
subject = Subject("Chemia", False)
subjects.append(subject)
subject = Subject("Fizyka", False)
subjects.append(subject)
subject = Subject("Wf", True)
subjects.append(subject)
subject = Subject("Informatyka", True)
subjects.append(subject)
subject = Subject("Religia", False)
subjects.append(subject)
subject = Subject("EDB", False)
subjects.append(subject)
subject = Subject("Plastyka", False)
subjects.append(subject)
subject = Subject("Godzina wychowawcza", False)
subjects.append(subject)

classrooms = []
classroom = Classroom("1", [findObject(subjects, "Angielski"), findObject(subjects, "Niemiecki"),
                            findObject(subjects, "Francuski")])
classrooms.append(classroom)
classroom = Classroom("11", [findObject(subjects, "Angielski"), findObject(subjects, "Niemiecki"),
                             findObject(subjects, "Francuski")])
classrooms.append(classroom)
classroom = Classroom("13", [findObject(subjects, "Angielski"), findObject(subjects, "Niemiecki"),
                             findObject(subjects, "Francuski")])
classrooms.append(classroom)
classroom = Classroom("21", [findObject(subjects, "Historia")])
classrooms.append(classroom)
classroom = Classroom("22", [findObject(subjects, "Polski")])
classrooms.append(classroom)
classroom = Classroom("23", [findObject(subjects, "Historia")])
classrooms.append(classroom)
classroom = Classroom("24", [findObject(subjects, "Matematyka")])
classrooms.append(classroom)
classroom = Classroom("27", [findObject(subjects, "Informatyka")])
classrooms.append(classroom)
classroom = Classroom("30", [findObject(subjects, "Biologia")])
classrooms.append(classroom)
classroom = Classroom("31", [findObject(subjects, "Informatyka")])
classrooms.append(classroom)
classroom = Classroom("32", [findObject(subjects, "Informatyka")])
classrooms.append(classroom)
classroom = Classroom("41", [findObject(subjects, "Matematyka")])
classrooms.append(classroom)
classroom = Classroom("42", [findObject(subjects, "Matematyka")])
classrooms.append(classroom)
classroom = Classroom("43", [findObject(subjects, "Chemia")])
classrooms.append(classroom)
classroom = Classroom("44", [findObject(subjects, "Chemia")])
classrooms.append(classroom)
classroom = Classroom("45", [findObject(subjects, "Chemia")])
classrooms.append(classroom)
classroom = Classroom("46", [findObject(subjects, "Polski")])
classrooms.append(classroom)
classroom = Classroom("52", [findObject(subjects, "Polski")])
classrooms.append(classroom)
classroom = Classroom("61", [findObject(subjects, "Biologia")])
classrooms.append(classroom)
classroom = Classroom("62", [findObject(subjects, "Biologia")])
classrooms.append(classroom)
classroom = Classroom("63", [findObject(subjects, "Angielski"), findObject(subjects, "Niemiecki"),
                             findObject(subjects, "Francuski")])
classrooms.append(classroom)
classroom = Classroom("64", [findObject(subjects, "Matematyka")])
classrooms.append(classroom)
classroom = Classroom("65", [findObject(subjects, "Geografia")])
classrooms.append(classroom)
classroom = Classroom("67", [findObject(subjects, "Fizyka")])
classrooms.append(classroom)
classroom = Classroom("68", [findObject(subjects, "Fizyka")])
classrooms.append(classroom)
classroom = Classroom("69", [findObject(subjects, "Fizyka")])
classrooms.append(classroom)
classroom = Classroom("81", [findObject(subjects, "Religia")])
classrooms.append(classroom)
classroom = Classroom("82", [findObject(subjects, "Niemiecki")])
classrooms.append(classroom)
classroom = Classroom("83", [findObject(subjects, "Niemiecki")])
classrooms.append(classroom)
classroom = Classroom("84", [findObject(subjects, "Angielski")])
classrooms.append(classroom)
classroom = Classroom("85", [findObject(subjects, "Francuski")])
classrooms.append(classroom)
classroom = Classroom("86", [findObject(subjects, "Angielski")])
classrooms.append(classroom)
classroom = Classroom("87", [])
classrooms.append(classroom)
classroom = Classroom("SG1", [findObject(subjects, "Wf")])
classrooms.append(classroom)
classroom = Classroom("SG2", [findObject(subjects, "Wf")])
classrooms.append(classroom)
classroom = Classroom("S", [findObject(subjects, "Wf")])
classrooms.append(classroom)
classroom = Classroom("T", [findObject(subjects, "Wf")])
classrooms.append(classroom)

teachers = []
# pol
teacher = Teacher("Katarzyna Bińkowska", [findObject(subjects, "Polski")])
teachers.append(teacher)
teacher = Teacher("Dorota Giedrojć", [findObject(subjects, "Polski")])
teachers.append(teacher)
teacher = Teacher("Anna Nakielska-Kowalska", [findObject(subjects, "Polski")])
teachers.append(teacher)
teacher = Teacher("Małgorzata Pielacka", [findObject(subjects, "Polski")])
teachers.append(teacher)
teacher = Teacher("Witold Uszyński", [findObject(subjects, "Polski")])
teachers.append(teacher)
teacher = Teacher("Irena Zielińska", [findObject(subjects, "Polski")])
teachers.append(teacher)
# ang
teacher = Teacher("Monika Izbaner", [findObject(subjects, "Angielski")])
teachers.append(teacher)
teacher = Teacher("Joanna Lisewska", [findObject(subjects, "Angielski")])
teachers.append(teacher)
teacher = Teacher("Maciej Müller", [findObject(subjects, "Angielski")])
teachers.append(teacher)
teacher = Teacher("Magdalena Pawlak", [findObject(subjects, "Angielski")])
teachers.append(teacher)
teacher = Teacher("Rafał Schaffrath", [findObject(subjects, "Angielski")])
teachers.append(teacher)
teacher = Teacher("Agnieszka Skrzypczyk", [findObject(subjects, "Angielski")])
teachers.append(teacher)
teacher = Teacher("Katarzyna Szewczyk-Koniarska", [findObject(subjects, "Angielski")])
teachers.append(teacher)
# franc
teacher = Teacher("Wiesława Burlińska", [findObject(subjects, "Francuski")])
teachers.append(teacher)
teacher = Teacher("Hanna Tholonias", [findObject(subjects, "Francuski")])
teachers.append(teacher)
teacher = Teacher("Agata Wnuk-Elbadry", [findObject(subjects, "Francuski")])
teachers.append(teacher)
# niem
teacher = Teacher("Anna Bukowska", [findObject(subjects, "Niemiecki")])
teachers.append(teacher)
teacher = Teacher("Małgorzata Kosek", [findObject(subjects, "Niemiecki")])
teachers.append(teacher)
teacher = Teacher("Adrian Sajna", [findObject(subjects, "Niemiecki")])
teachers.append(teacher)
teacher = Teacher("Marta Szreiber", [findObject(subjects, "Niemiecki")])
teachers.append(teacher)
# matma
teacher = Teacher("Dorota Dulińska", [findObject(subjects, "Matematyka")])
teachers.append(teacher)
teacher = Teacher("Anna Karaszewska", [findObject(subjects, "Matematyka")])
teachers.append(teacher)
teacher = Teacher("Zofia Olędzka", [findObject(subjects, "Matematyka"), findObject(subjects, "Informatyka")])
teachers.append(teacher)
teacher = Teacher("Ewa Politycka-Proczek", [findObject(subjects, "Matematyka")])
teachers.append(teacher)
teacher = Teacher("Bernadeta Szmańda", [findObject(subjects, "Matematyka")])
teachers.append(teacher)
teacher = Teacher("Michał Wenderlich", [findObject(subjects, "Matematyka"), findObject(subjects, "Informatyka")])
teachers.append(teacher)
# geo
teacher = Teacher("Wojciech Olejniczak", [findObject(subjects, "Geografia")])
teachers.append(teacher)
# PP
teacher = Teacher("Katarzyna Sobczak",
                  [findObject(subjects, "Podstawy przedsiębiorczości"), findObject(subjects, "Informatyka")])
teachers.append(teacher)
# his/wos
teacher = Teacher("Jolanta Kaźmierczak", [findObject(subjects, "Historia"), findObject(subjects, "WOS")])
teachers.append(teacher)
teacher = Teacher("Krzysztof Kłosowski", [findObject(subjects, "Historia"), findObject(subjects, "WOS")])
teachers.append(teacher)
teacher = Teacher("Nel Powel", [findObject(subjects, "Historia"), findObject(subjects, "WOS")])
teachers.append(teacher)
teacher = Teacher("Grzegorz Śliwiński", [findObject(subjects, "Historia"), findObject(subjects, "WOS")])
teachers.append(teacher)
# Biol
teacher = Teacher("Barbara Ciechalska", [findObject(subjects, "Biologia")])
teachers.append(teacher)
teacher = Teacher("Małgorzata Jeske", [findObject(subjects, "Biologia")])
teachers.append(teacher)
teacher = Teacher("Joanna Juryś", [findObject(subjects, "Biologia")])
teachers.append(teacher)
teacher = Teacher("Agnieszka Mądzielewska-Jagodzińska", [findObject(subjects, "Biologia")])
teachers.append(teacher)
teacher = Teacher("Iwona Paprzycka", [findObject(subjects, "Biologia")])
teachers.append(teacher)
teacher = Teacher("Renata Starczewska-Bieńkowska", [findObject(subjects, "Biologia")])
teachers.append(teacher)
# chemia
teacher = Teacher("Joanna Cieślewicz", [findObject(subjects, "Chemia")])
teachers.append(teacher)
teacher = Teacher("Agnieszka Grzelakowska", [findObject(subjects, "Chemia")])
teachers.append(teacher)
teacher = Teacher("Agnieszka Łysio", [findObject(subjects, "Chemia")])
teachers.append(teacher)
teacher = Teacher("Anna Wieczór", [findObject(subjects, "Chemia")])
teachers.append(teacher)
# fiz
teacher = Teacher("Romaric Abdoul", [findObject(subjects, "Fizyka")])
teachers.append(teacher)
teacher = Teacher("Piotr Malinowski", [findObject(subjects, "Fizyka")])
teachers.append(teacher)
teacher = Teacher("Grzegorz Wojewoda", [findObject(subjects, "Fizyka")])
teachers.append(teacher)
# WF
teacher = Teacher("Izabela Kotecka", [findObject(subjects, "Wf")])
teachers.append(teacher)
teacher = Teacher("Jakub Lewandowski", [findObject(subjects, "Wf")])
teachers.append(teacher)
teacher = Teacher("Lucyna Ligaj-Stankiewicz", [findObject(subjects, "Wf")])
teachers.append(teacher)
teacher = Teacher("Krzysztof Lubiński", [findObject(subjects, "Wf")])
teachers.append(teacher)
teacher = Teacher("Miłosława Roś", [findObject(subjects, "Wf"), findObject(subjects, "EDB")])
teachers.append(teacher)
teacher = Teacher("Aleksandra Szałajda", [findObject(subjects, "Wf")])
teachers.append(teacher)
teacher = Teacher("Katarzyna Warczak", [findObject(subjects, "Wf")])
teachers.append(teacher)
# inf
teacher = Teacher("Krzysztof Hyżyk", [findObject(subjects, "Informatyka")])
teachers.append(teacher)
teacher = Teacher("Małgorzata Piekarska", [findObject(subjects, "Informatyka")])
teachers.append(teacher)
# religia
teacher = Teacher("Grzegorz Duchnik", [findObject(subjects, "Religia")])
teachers.append(teacher)
teacher = Teacher("Tomasz Poćwiardowski", [findObject(subjects, "Religia")])
teachers.append(teacher)
teacher = Teacher("Marzena Prochowska", [findObject(subjects, "Religia")])
teachers.append(teacher)
# rys/plast
teacher = Teacher("Agnieszka Markowska", [findObject(subjects, "Plastyka")])
teachers.append(teacher)
# spr czy nauczyciele sie powtarzaja
# powt=[]
# for i in range(0,len(teachers)):
#    for j in range(i+1, len(teachers)):
#       if teachers[i].name==teachers[j].name:
#          powt.append(teachers[i])
# for i in powt:
#    print(i.name)

classes = []
# przedmiot, rozszerzenie, liczba godzin
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Katarzyna Bińkowska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Magdalena Pawlak")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Małgorzata Kosek")],
                    [findObject(subjects, "Plastyka"), False, 1, findObject(teachers, "Agnieszka Markowska")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Grzegorz Śliwiński")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Grzegorz Śliwiński")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Iwona Paprzycka")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Joanna Cieślewicz")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Romaric Abdoul")],
                    [findObject(subjects, "Fizyka"), True, 1, findObject(teachers, "Romaric Abdoul")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Dorota Dulińska")],
                    [findObject(subjects, "Matematyka"), True, 2, findObject(teachers, "Dorota Dulińska")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Małgorzata Piekarska")],
                    [findObject(subjects, "Informatyka"), True, 1, findObject(teachers,"Małgorzata Piekarska")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Izabela Kotecka")],
                    [findObject(subjects, "EDB"), False, 1, findObject(teachers, "Miłosława Roś")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Katarzyna Bińkowska")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Grzegorz Duchnik")]]
classUnit = Class("1a", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Katarzyna Bińkowska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Magdalena Pawlak")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Małgorzata Kosek")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Grzegorz Śliwiński")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Grzegorz Śliwiński")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 2, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 2, findObject(teachers, "Iwona Paprzycka")],
                    [findObject(subjects, "Chemia"), False, 2, findObject(teachers, "Joanna Cieślewicz")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Romaric Abdoul")],
                    [findObject(subjects, "Fizyka"), True, 2, findObject(teachers, "Romaric Abdoul")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Dorota Dulińska")],
                    [findObject(subjects, "Matematyka"), True, 1, findObject(teachers, "Dorota Dulińska")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Krzysztof Hyżyk")],
                    [findObject(subjects, "Informatyka"), True, 1, findObject(teachers,"Krzysztof Hyżyk")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Izabela Kotecka")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Magdalena Pawlak")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Grzegorz Duchnik")]]
classUnit = Class("2a", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Katarzyna Bińkowska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Magdalena Pawlak")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Małgorzata Kosek")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Grzegorz Śliwiński")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Iwona Paprzycka")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Joanna Cieślewicz")],
                    [findObject(subjects, "Fizyka"), False, 2, findObject(teachers, "Romaric Abdoul")],
                    [findObject(subjects, "Fizyka"), True, 1, findObject(teachers, "Romaric Abdoul")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Dorota Dulińska")],
                    [findObject(subjects, "Matematyka"), True, 2, findObject(teachers, "Dorota Dulińska")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Informatyka"), True, 2, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Izabela Kotecka")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Małgorzata Kosek")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Grzegorz Duchnik")]]
classUnit = Class("3a", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Katarzyna Bińkowska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Agnieszka Skrzypczyk")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Małgorzata Kosek")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Grzegorz Śliwiński")],
                    [findObject(subjects, "Fizyka"), True, 2, findObject(teachers, "Romaric Abdoul")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Dorota Dulińska")],
                    [findObject(subjects, "Matematyka"), True, 1, findObject(teachers, "Dorota Dulińska")],
                    [findObject(subjects, "Informatyka"), True, 2, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Jakub Lewandowski")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Agnieszka Skrzypczyk")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Grzegorz Duchnik")]]
classUnit = Class("4a", list_of_subjects)
classes.append(classUnit)

list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Dorota Giedrojć")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Rafał Schaffrath")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Małgorzata Kosek")],
                    [findObject(subjects, "Plastyka"), False, 1, findObject(teachers, "Agnieszka Markowska")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Grzegorz Śliwiński")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Grzegorz Śliwiński")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Małgorzata Jeske")],
                    [findObject(subjects, "Biologia"), True, 2, findObject(teachers, "Barbara Ciechalska")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Joanna Cieślewicz")],
                    [findObject(subjects, "Chemia"), True, 2, findObject(teachers, "Agnieszka Łysio")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Romaric Abdoul")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Anna Karaszewska")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Michał Wenderlich")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Jakub Lewandowski")],
                    [findObject(subjects, "EDB"), False, 1, findObject(teachers, "Miłosława Roś")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Dorota Giedrojć")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Grzegorz Duchnik")]]
classUnit = Class("1b", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Dorota Giedrojć")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Rafał Schaffrath")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Małgorzata Kosek")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Grzegorz Śliwiński")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Nel Powel")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 2, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 2, findObject(teachers, "Małgorzata Jeske")],
                    [findObject(subjects, "Biologia"), True, 3, findObject(teachers, "Barbara Ciechalska")],
                    [findObject(subjects, "Chemia"), False, 2, findObject(teachers, "Joanna Cieślewicz")],
                    [findObject(subjects, "Chemia"), True, 2, findObject(teachers, "Agnieszka Łysio")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Romaric Abdoul")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Anna Karaszewska")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Michał Wenderlich")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Jakub Lewandowski")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Grzegorz Śliwiński")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Grzegorz Duchnik")]]
classUnit = Class("2b", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Dorota Giedrojć")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Rafał Schaffrath")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Adrian Sajna")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Jolanta Kaźmierczak")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Małgorzata Jeske")],
                    [findObject(subjects, "Biologia"), True, 3, findObject(teachers, "Iwona Paprzycka")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Joanna Cieślewicz")],
                    [findObject(subjects, "Chemia"), True, 4, findObject(teachers, "Agnieszka Łysio")],
                    [findObject(subjects, "Fizyka"), False, 2, findObject(teachers, "Piotr Malinowski")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Anna Karaszewska")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Michał Wenderlich")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Lucyna Ligaj-Stankiewicz")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Grzegorz Duchnik")]]
classUnit = Class("3b", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Dorota Giedrojć")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Agnieszka Skrzypczyk")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Adrian Sajna")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Jolanta Kaźmierczak")],
                    [findObject(subjects, "Biologia"), True, 3, findObject(teachers, "Iwona Paprzycka")],
                    [findObject(subjects, "Chemia"), True, 3, findObject(teachers, "Agnieszka Łysio")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Anna Karaszewska")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Lucyna Ligaj-Stankiewicz")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Adrian Sajna")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Grzegorz Duchnik")]]
classUnit = Class("4b", list_of_subjects)
classes.append(classUnit)

list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Anna Nakielska-Kowalska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Katarzyna Szewczyk-Koniarska")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Marta Szreiber")],
                    [findObject(subjects, "Plastyka"), False, 1, findObject(teachers, "Agnieszka Markowska")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Jolanta Kaźmierczak")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Nel Powel")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Małgorzata Jeske")],
                    [findObject(subjects, "Biologia"), True, 2, findObject(teachers, "Barbara Ciechalska")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Joanna Cieślewicz")],
                    [findObject(subjects, "Chemia"), True, 2, findObject(teachers, "Agnieszka Łysio")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Piotr Malinowski")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Anna Karaszewska")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Zofia Olędzka")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Lucyna Ligaj-Stankiewicz")],
                    [findObject(subjects, "EDB"), False, 1, findObject(teachers, "Miłosława Roś")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Nel Powel")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Tomasz Poćwiardowski")]]
classUnit = Class("1c", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Anna Nakielska-Kowalska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Katarzyna Szewczyk-Koniarska")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Marta Szreiber")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Jolanta Kaźmierczak")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Nel Powel")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 2, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 2, findObject(teachers, "Małgorzata Jeske")],
                    [findObject(subjects, "Biologia"), True, 3, findObject(teachers, "Barbara Ciechalska")],
                    [findObject(subjects, "Chemia"), False, 2, findObject(teachers, "Anna Wieczór")],
                    [findObject(subjects, "Chemia"), True, 2, findObject(teachers, "Agnieszka Łysio")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Piotr Malinowski")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Zofia Olędzka")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Zofia Olędzka")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Krzysztof Lubiński")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Anna Nakielska-Kowalska")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Tomasz Poćwiardowski")]]
classUnit = Class("2c", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Anna Nakielska-Kowalska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Katarzyna Szewczyk-Koniarska")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Marta Szreiber")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Jolanta Kaźmierczak")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Joanna Juryś")],
                    [findObject(subjects, "Biologia"), True, 3, findObject(teachers, "Renata Starczewska-Bieńkowska")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Anna Wieczór")],
                    [findObject(subjects, "Chemia"), True, 4, findObject(teachers, "Agnieszka Łysio")],
                    [findObject(subjects, "Fizyka"), False, 2, findObject(teachers, "Piotr Malinowski")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Zofia Olędzka")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Zofia Olędzka")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Krzysztof Lubiński")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Piotr Malinowski")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Tomasz Poćwiardowski")]]
classUnit = Class("3c", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Anna Nakielska-Kowalska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Agnieszka Skrzypczyk")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Marta Szreiber")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Jolanta Kaźmierczak")],
                    [findObject(subjects, "Biologia"), True, 3, findObject(teachers, "Renata Starczewska-Bieńkowska")],
                    [findObject(subjects, "Chemia"), True, 3, findObject(teachers, "Agnieszka Łysio")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Zofia Olędzka")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Krzysztof Lubiński")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Zofia Olędzka")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Tomasz Poćwiardowski")]]
classUnit = Class("4c", list_of_subjects)
classes.append(classUnit)

list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Małgorzata Pielacka")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Maciej Müller")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Marta Szreiber")],
                    [findObject(subjects, "Plastyka"), False, 1, findObject(teachers, "Agnieszka Markowska")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Krzysztof Kłosowski")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Krzysztof Kłosowski")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Joanna Juryś")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Anna Wieczór")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Piotr Malinowski")],
                    [findObject(subjects, "Fizyka"), True, 1, findObject(teachers, "Piotr Malinowski")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Bernadeta Szmańda")],
                    [findObject(subjects, "Matematyka"), True, 2, findObject(teachers, "Bernadeta Szmańda")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Małgorzata Piekarska")],
                    [findObject(subjects, "Informatyka"), True, 1, findObject(teachers,"Małgorzata Piekarska")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Krzysztof Lubiński")],
                    [findObject(subjects, "EDB"), False, 1, findObject(teachers, "Miłosława Roś")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Joanna Juryś")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Tomasz Poćwiardowski")]]
classUnit = Class("1d", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Małgorzata Pielacka")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Maciej Müller")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Marta Szreiber")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Krzysztof Kłosowski")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Krzysztof Kłosowski")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 2, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 2, findObject(teachers, "Joanna Juryś")],
                    [findObject(subjects, "Chemia"), False, 2, findObject(teachers, "Anna Wieczór")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Piotr Malinowski")],
                    [findObject(subjects, "Fizyka"), True, 2, findObject(teachers, "Piotr Malinowski")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Zofia Olędzka")],
                    [findObject(subjects, "Matematyka"), True, 1, findObject(teachers, "Zofia Olędzka")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Małgorzata Piekarska")],
                    [findObject(subjects, "Informatyka"), True, 1, findObject(teachers,"Małgorzata Piekarska")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Miłosława Roś")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Małgorzata Piekarska")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Tomasz Poćwiardowski")]]
classUnit = Class("2d", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Małgorzata Pielacka")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Maciej Müller")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Adrian Sajna")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Krzysztof Kłosowski")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Joanna Juryś")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Anna Wieczór")],
                    [findObject(subjects, "Fizyka"), False, 2, findObject(teachers, "Grzegorz Wojewoda")],
                    [findObject(subjects, "Fizyka"), True, 1, findObject(teachers, "Grzegorz Wojewoda")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Ewa Politycka-Proczek")],
                    [findObject(subjects, "Matematyka"), True, 2, findObject(teachers, "Ewa Politycka-Proczek")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Krzysztof Hyżyk" )],
                    [findObject(subjects, "Informatyka"), True, 2, findObject(teachers,"Krzysztof Hyżyk" )],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Miłosława Roś")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Grzegorz Wojewoda")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Tomasz Poćwiardowski")]]
classUnit = Class("3d", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Małgorzata Pielacka")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Maciej Müller")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Adrian Sajna")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Krzysztof Kłosowski")],
                    [findObject(subjects, "Fizyka"), True, 2, findObject(teachers, "Grzegorz Wojewoda")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Ewa Politycka-Proczek")],
                    [findObject(subjects, "Matematyka"), True, 1, findObject(teachers, "Ewa Politycka-Proczek")],
                    [findObject(subjects, "Informatyka"), True, 2, findObject(teachers,"Krzysztof Hyżyk" )],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Miłosława Roś")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Maciej Müller")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Tomasz Poćwiardowski")]]
classUnit = Class("4d", list_of_subjects)
classes.append(classUnit)

list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Irena Zielińska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Joanna Lisewska")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Anna Bukowska")],
                    [findObject(subjects, "Plastyka"), False, 1, findObject(teachers, "Agnieszka Markowska")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Nel Powel")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Krzysztof Kłosowski")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Joanna Juryś")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Anna Wieczór")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Grzegorz Wojewoda")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Ewa Politycka-Proczek")],
                    [findObject(subjects, "Matematyka"), True, 1, findObject(teachers, "Ewa Politycka-Proczek")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Informatyka"), True, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Aleksandra Szałajda")],
                    [findObject(subjects, "EDB"), False, 1, findObject(teachers, "Miłosława Roś")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Ewa Politycka-Proczek")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Marzena Prochowska")]]
classUnit = Class("1e", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Irena Zielińska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Joanna Lisewska")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Anna Bukowska")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Nel Powel")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Jolanta Kaźmierczak")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 2, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 2, findObject(teachers, "Agnieszka Mądzielewska-Jagodzińska")],
                    [findObject(subjects, "Chemia"), False, 2, findObject(teachers, "Anna Wieczór")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Grzegorz Wojewoda")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Ewa Politycka-Proczek")],
                    [findObject(subjects, "Matematyka"), True, 1, findObject(teachers, "Ewa Politycka-Proczek")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Michał Wenderlich")],
                    [findObject(subjects, "Informatyka"), True, 2, findObject(teachers,"Michał Wenderlich")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Aleksandra Szałajda")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Michał Wenderlich")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Marzena Prochowska")]]
classUnit = Class("2e", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Irena Zielińska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Joanna Lisewska")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Adrian Sajna")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Krzysztof Kłosowski")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Agnieszka Mądzielewska-Jagodzińska")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Agnieszka Grzelakowska")],
                    [findObject(subjects, "Fizyka"), False, 2, findObject(teachers, "Grzegorz Wojewoda")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Bernadeta Szmańda")],
                    [findObject(subjects, "Matematyka"), True, 2, findObject(teachers, "Bernadeta Szmańda")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Zofia Olędzka")],
                    [findObject(subjects, "Informatyka"), True, 2, findObject(teachers,"Zofia Olędzka")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Aleksandra Szałajda")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Irena Zielińska")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Marzena Prochowska")]]
classUnit = Class("3e", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Irena Zielińska")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Joanna Lisewska")],
                    [findObject(subjects, "Francuski"), False, 2, findObject(teachers, "Adrian Sajna")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Krzysztof Kłosowski")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Bernadeta Szmańda")],
                    [findObject(subjects, "Matematyka"), True, 2, findObject(teachers, "Bernadeta Szmańda")],
                    [findObject(subjects, "Informatyka"), True, 2, findObject(teachers,"Małgorzata Piekarska")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers,"Aleksandra Szałajda")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Bernadeta Szmańda")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Marzena Prochowska")]]
classUnit = Class("4e", list_of_subjects)
classes.append(classUnit)

list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Witold Uszyński")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Monika Izbaner")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Anna Bukowska")],
                    [findObject(subjects, "Plastyka"), False, 1, findObject(teachers, "Agnieszka Markowska")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Nel Powel")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Jolanta Kaźmierczak")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Agnieszka Mądzielewska-Jagodzińska")],
                    [findObject(subjects, "Biologia"), True, 1, findObject(teachers, "Barbara Ciechalska")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Agnieszka Grzelakowska")],
                    [findObject(subjects, "Chemia"), True, 1, findObject(teachers, "Agnieszka Grzelakowska")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Grzegorz Wojewoda")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Bernadeta Szmańda")],
                    [findObject(subjects, "Matematyka"), True, 2, findObject(teachers, "Bernadeta Szmańda")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Krzysztof Hyżyk")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers, "Katarzyna Warczak")],
                    [findObject(subjects, "EDB"), False, 1, findObject(teachers, "Miłosława Roś")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Anna Bukowska")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Marzena Prochowska")]]
classUnit = Class("1f", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Witold Uszyński")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Monika Izbaner")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Anna Bukowska")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Nel Powel")],
                    [findObject(subjects, "WOS"), False, 1, findObject(teachers, "Jolanta Kaźmierczak")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 2, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 2, findObject(teachers, "Agnieszka Mądzielewska-Jagodzińska")],
                    [findObject(subjects, "Biologia"), True, 2, findObject(teachers, "Renata Starczewska-Bieńkowska")],
                    [findObject(subjects, "Chemia"), False, 2, findObject(teachers, "Agnieszka Grzelakowska")],
                    [findObject(subjects, "Chemia"), True, 2, findObject(teachers, "Agnieszka Grzelakowska")],
                    [findObject(subjects, "Fizyka"), False, 1, findObject(teachers, "Grzegorz Wojewoda")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Michał Wenderlich")],
                    [findObject(subjects, "Matematyka"), True, 1, findObject(teachers, "Michał Wenderlich")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers, "Katarzyna Warczak")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Katarzyna Warczak")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Marzena Prochowska")]]
classUnit = Class("2f", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Witold Uszyński")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Monika Izbaner")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Anna Bukowska")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Nel Powel")],
                    [findObject(subjects, "Podstawy przedsiębiorczości"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Geografia"), False, 1, findObject(teachers, "Wojciech Olejniczak")],
                    [findObject(subjects, "Biologia"), False, 1, findObject(teachers, "Agnieszka Mądzielewska-Jagodzińska")],
                    [findObject(subjects, "Biologia"), True, 3, findObject(teachers, "Renata Starczewska-Bieńkowska")],
                    [findObject(subjects, "Chemia"), False, 1, findObject(teachers, "Agnieszka Grzelakowska")],
                    [findObject(subjects, "Chemia"), True, 2, findObject(teachers, "Agnieszka Grzelakowska")],
                    [findObject(subjects, "Fizyka"), False, 2, findObject(teachers, "Grzegorz Wojewoda")],
                    [findObject(subjects, "Matematyka"), False, 3, findObject(teachers, "Michał Wenderlich")],
                    [findObject(subjects, "Matematyka"), True, 2, findObject(teachers, "Michał Wenderlich")],
                    [findObject(subjects, "Informatyka"), False, 1, findObject(teachers,"Katarzyna Sobczak")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers, "Katarzyna Warczak")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Agnieszka Mądzielewska-Jagodzińska")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Marzena Prochowska")]]
classUnit = Class("3f", list_of_subjects)
classes.append(classUnit)
list_of_subjects = [[findObject(subjects, "Polski"), False, 4, findObject(teachers, "Witold Uszyński")],
                    [findObject(subjects, "Angielski"), False, 3, findObject(teachers, "Monika Izbaner")],
                    [findObject(subjects, "Niemiecki"), False, 2, findObject(teachers, "Anna Bukowska")],
                    [findObject(subjects, "Historia"), False, 2, findObject(teachers, "Nel Powel")],
                    [findObject(subjects, "Biologia"), True, 2, findObject(teachers, "Renata Starczewska-Bieńkowska")],
                    [findObject(subjects, "Chemia"), True, 3, findObject(teachers, "Agnieszka Grzelakowska")],
                    [findObject(subjects, "Matematyka"), False, 4, findObject(teachers, "Michał Wenderlich")],
                    [findObject(subjects, "Matematyka"), True, 1, findObject(teachers, "Michał Wenderlich")],
                    [findObject(subjects, "Wf"), False, 3, findObject(teachers, "Katarzyna Warczak")],
                    [findObject(subjects, "Godzina wychowawcza"), False, 1, findObject(teachers, "Krzysztof Lubiński")],
                    [findObject(subjects, "Religia"), False, 2, findObject(teachers, "Marzena Prochowska")]]
classUnit = Class("4f", list_of_subjects)
classes.append(classUnit)


# for s in subjects:
#     s.printName()
#
# for c in classrooms:
#     c.printNumber()
#
# for c in classes:
#     c.printName()
#
# for t in teachers:
#     t.printName()

# for s in subjects:
#     print(s.toString())
#
# for c in classrooms:
#      print(c.toString())
#
for c in classes:
     print(c.toString())
#
# for t in teachers:
#     print(t.toString())

