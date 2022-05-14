import os
from prettytable import PrettyTable
from data import *
import random
from copy import deepcopy

rewardClassroomType = 0.5
rewardPreferredHours = 0.1
punishmentClassroomType = -1
punishmentTwoAtTheTime = -10
punishmentGap = -0.1
punishmentGapLength = -0.3

x = PrettyTable()

def getRandomObject(objects):
    size = len(objects)
    r = random.randint(0, size - 1)
    obj = objects[r]
    return obj

def getRandomClassroom(subject):
    potentialClassrooms = []
    for cl in classrooms:
        if findObject(subjects, "Wf") not in cl.preferred_subject_list:
            potentialClassrooms.append(cl)
    classroom = getRandomObject(potentialClassrooms)
    return classroom

def randomDayAndHour():
    randomDay = random.randint(0, len(days) - 1)
    randomHour = random.randint(0, len(hours) - 1)
    return randomDay, randomHour

def printLesson(lesson):
    lesson[0].printName()
    lesson[1].printName()
    lesson[2].printName()
    print(days[lesson[3]], end=' ')
    print(hours[lesson[4]], end=' ')
    lesson[5].printNumber()

def lessonToString(lesson):
    s = lesson[0].name
    s += " "
    s += lesson[1].name
    s += " "
    s += lesson[2].name
    s += " "
    s += days[lesson[3]]
    s += " "
    s += hours[lesson[4]]
    s += " "
    s += lesson[5].number
    return s

def planToString(plan):
    planString = ""
    for lessons in plan:
        planString += "["
        for lessonHour in lessons:
            planString += "["
            for lesson in lessonHour:
                planString += lessonToString(lesson)
                planString += "; "
            planString += "]\n"
        planString += "]\n"
    return planString

def generatePlan():
    plan = [[[] for j in range(len(hours))] for i in range(len(days))]
    for classUnit in classes:
        for s in classUnit.subject_list:
            for nrOfHours in range(s[2]):
                lesson = []
                lesson.append(classUnit) #class
                lesson.append(s[0]) #subject
                lesson.append(s[3]) #teacher
                day, hour = randomDayAndHour()
                lesson.append(day) #day
                lesson.append(hour) #hour
                lesson.append(getRandomClassroom(s[0])) #classroom
                plan[day][hour].append(lesson)
    #print(planString)
    return plan

def checkClassrooms(pl):
    fitness = 0
    hardProblemsCount = 0
    for day in pl:
        for hour in day:
            for lesson in hour:
                if lesson[1].necessary_classroom_type:
                    if lesson[1] in lesson[5].preferred_subject_list:
                        fitness += rewardClassroomType
                    else:
                        fitness += punishmentClassroomType
                        hardProblemsCount += 1
                else:
                    if lesson[1] in lesson[5].preferred_subject_list:
                        fitness += rewardClassroomType
    return fitness, hardProblemsCount

def checkOneAtTheTime(pl):
    fitness = 0
    hardProblemsCount = 0
    for day in pl:
        for hour in day:
            classList = []
            classroomList = []
            teacherList = []
            for lesson in hour:
                if lesson[0] not in classList:
                    classList.append(lesson[0])
                else:
                    fitness += punishmentTwoAtTheTime
                    hardProblemsCount += 1
                if lesson[5] not in classroomList:
                    classroomList.append(lesson[5])
                else:
                    fitness += punishmentTwoAtTheTime
                    hardProblemsCount += 1
                if lesson[2] not in teacherList:
                    teacherList.append(lesson[2])
                else:
                    fitness += punishmentTwoAtTheTime
                    hardProblemsCount += 1
    return fitness, hardProblemsCount

def plansForClasses(pl):
    classesPlans = [[[[] for j in range(len(hours))] for i in range(len(days))] for k in range(len(classes))]
    for planDay in pl:
        for planHour in planDay:
            for lesson in planHour:
                classIndex = classes.index(findObject(classes, lesson[0].name))
                classesPlans[classIndex][lesson[3]][lesson[4]].append(lesson)
    return classesPlans

def checkGapsAndPreferredHours(classesPlans):
    fitness = 0
    hardProblemsCount = 0
    for cl in classesPlans:
        for day in cl:
            gaps = 0
            classHappened = False
            currentGap = 0
            for hour in day:
                if len(hour) != 0:
                    if classHappened:
                        gaps += currentGap
                        currentGap = 0
                        if currentGap > 2:
                           fitness += punishmentGapLength
                    classHappened = True
                else:
                    currentGap += 1

                if day.index(hour) >= 3 and day.index(hour) <= 8 and len(hour) != 0:
                    fitness += rewardPreferredHours
            fitness += punishmentGap * gaps
    return fitness, hardProblemsCount

def checkFitness(pl, printing):
    classesPlans = plansForClasses(pl)
    fitnesses = 0
    hardProblemsCount = 0

    fitTmp, hardProbTmp = checkClassrooms(pl)
    fitnesses += fitTmp
    hardProblemsCount += hardProbTmp

    fitTmp, hardProbTmp = checkOneAtTheTime(pl)
    fitnesses += fitTmp
    hardProblemsCount += hardProbTmp

    fitTmp, hardProbTmp = checkGapsAndPreferredHours(classesPlans)
    fitnesses += fitTmp
    hardProblemsCount += hardProbTmp

    if printing:
        print("Fitness: {:.2f}".format(fitnesses), ", Hard problems: ", hardProblemsCount)
    return fitnesses

def saveToFile():
    file = open("bestIndividuals.txt", "w")
    for pl in bestIndividuals:
        file.write(";\n")
        for day in pl:
            for hour in day:
                for lesson in hour:
                    file.write(lesson[0].name + "\n")
                    file.write(lesson[1].name + "\n")
                    file.write(lesson[2].name + "\n")
                    file.write(str(lesson[3]) + "\n")
                    file.write(str(lesson[4]) + "\n")
                    file.write(lesson[5].number + "\n")
    file.write(";\n")
    file.close()

def readFromFile():
    with open("bestIndividuals.txt") as file:
        lines = file.read().splitlines()
    indexCounter = 0
    lesson = []
    flag = 0
    for line in lines:
        if line == ";":
            if flag == 1:
                plans.append(plan)
            flag = 1
            plan = [[[] for j in range(len(hours))] for i in range(len(days))]
        else:
            if indexCounter == 0:
                lesson.append(findObject(classes, line))
            elif indexCounter == 1:
                lesson.append(findObject(subjects, line))
            elif indexCounter == 2:
                lesson.append(findObject(teachers, line))
            elif indexCounter == 3 or indexCounter == 4:
                lesson.append(int(line))
            elif indexCounter == 5:
                for obj in classrooms:
                    if obj.number == line:
                        lesson.append(obj)
                        break
            if indexCounter == 5:
                indexCounter = -1
                plan[lesson[3]][lesson[4]].append(lesson)
                lesson = []
            indexCounter += 1

def sort(newPlans, points):
    points = fitnessPoints(newPlans)
    n = len(newPlans)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if points[j] > points[j + 1]:
                newPlans[j], newPlans[j + 1] = newPlans[j + 1], newPlans[j]
                points[j], points[j + 1] = points[j + 1], points[j]
    return newPlans, points

def fitnessPoints(plans):
    points = []
    for pl in range(numberOfIndividuals):
        points.append(checkFitness(plans[pl], False))
    return points

def top10(plans, points):
    plans, points = sort(plans, points)
    for pl in range(len(plans) - 10, len(plans)):
        print(points[pl],end=" ")
        checkFitness(plans[pl], True)

def saveBestIndividuals(plans, points):
    if(len(bestIndividuals) == 0):
        for i in range(len(plans)):
            bestIndividuals.append(plans[i].copy())
            bestPoints.append(points[i])
    else:
        for pl in range(len(bestIndividuals)):
            if points[-1] > bestPoints[pl]:
                bestIndividuals[pl] = plans[-1].copy()
                bestPoints[pl] = points[-1]
                break

def reproduction(plans, points):
    nrOfCopiesToSelect = int(numberOfIndividuals * selection_factor)
    nrOfEliteCopies = int(numberOfIndividuals * elitarism_factor)
    plans, points = sort(plans, points)
    saveBestIndividuals(plans, points)
    for i in range(nrOfCopiesToSelect):
        plans[i] = deepcopy(plans[numberOfIndividuals - i - 1])
        points[i] = points[numberOfIndividuals - i - 1]

    for pl in range(nrOfEliteCopies):
        elitePlans.append(deepcopy(plans[numberOfIndividuals - pl - 1]))

    for pl in range(int(numberOfIndividuals * elitarism_factor)):
        elitePoints.append(checkFitness(elitePlans[pl], False))
    return plans

def crossover(plans):
    for plan in plans:
        r = random.random()
        if r < pCrossover:
            randomDay = plan[random.randint(0, len(days) - 1)]
            randomHour = randomDay[random.randint(0, len(randomDay) - 1)]
            while(len(randomHour) == 0):
                randomDay = plan[random.randint(0, len(days) - 1)]
                randomHour = randomDay[random.randint(0, len(randomDay) - 1)]
            randomLesson = randomHour[random.randint(0, len(randomHour) - 1)]
            randomPlan = plans[random.randint(0, len(plans) - 1)]
            fittingLessons = []
            for lessonDays in range(len(randomPlan)):
                for lessonHours in range(len(randomPlan[lessonDays])):
                    for les in randomPlan[lessonDays][lessonHours]:
                        if les[0].name == randomLesson[0].name and les[1].name == randomLesson[1].name and les[2].name == randomLesson[2].name:
                            fittingLessons.append(les)
            fittingLesson = fittingLessons[random.randint(0, len(fittingLessons) - 1)]
            fitness1 = checkFitness(plan, False)
            fitness2 = checkFitness(randomPlan, False)
            if (fitness1 > fitness2):
                #fittingLesson z randomPlan = randomLesson z plan
                r = random.random()
                if r > 0.5: #zmiana dnia i godziny fittingLesson na randomLesson
                    # lesson = fittingLesson.copy()
                    lesson = deepcopy(fittingLesson)
                    lesson[3] = randomLesson[3]
                    lesson[4] = randomLesson[4]
                    randomPlan[fittingLesson[3]][fittingLesson[4]].remove(fittingLesson)
                    randomPlan[lesson[3]][lesson[4]].append(lesson)
                else: #zmiana sali z fittingLesson na randomLesson
                    fittingLesson[5] = randomLesson[5]
            else:
                #randomLesson z plan = fittingLesson z randomPlan
                r = random.random()
                if r > 0.5: #zmiana dnia i godziny randomLesson na fittingLesson
                    # lesson = randomLesson.copy()
                    lesson = deepcopy(randomLesson)
                    lesson[3] = fittingLesson[3]
                    lesson[4] = fittingLesson[4]
                    plan[randomLesson[3]][randomLesson[4]].remove(randomLesson)
                    plan[lesson[3]][lesson[4]].append(lesson)
                else: #zmiana sali z randomLesson na fittingLesson
                    randomLesson[5] = fittingLesson[5]
    return plans

def mutation(plans):
    for pl in plans:
        r = random.random()
        if (r < pMutation):
            for lessonDays in range(len(pl)):
                for lessonHours in range(len(pl[lessonDays])):
                    for les in pl[lessonDays][lessonHours]:
                        lesson = deepcopy(les)
                        r = random.random()
                        if (r < 0.5):
                            day, hour = randomDayAndHour()  # lesson at other time
                            lesson[3] = day
                            lesson[4] = hour
                            pl[day][hour].append(lesson)
                            pl[lessonDays][lessonHours].remove(les)
                        else:
                            lesson[5] = getRandomClassroom(lesson[1])  # other classroom
    return plans

def laterMutation(plans):
    for plan in plans:
        r = random.random()
        if (r < pMutation):
            randomDay = plan[random.randint(0, len(days) - 1)]
            randomHour = randomDay[random.randint(0, len(randomDay) - 1)]
            while (len(randomHour) == 0):
                randomDay = plan[random.randint(0, len(days) - 1)]
                randomHour = randomDay[random.randint(0, len(randomDay) - 1)]
            les = randomHour[random.randint(0, len(randomHour) - 1)]
            lesson = deepcopy(les)
            r = random.random()
            if (r < 0.5):
                day, hour = randomDayAndHour()  # lesson at other time
                lesson[3] = day
                lesson[4] = hour
                plan[day][hour].append(lesson)
                plan[les[3]][les[4]].remove(les)
            else:
                lesson[5] = getRandomClassroom(lesson[1])  # other classroom
    return plans

numberOfIndividuals = 100
numberOfEpochs = 1000
pCrossover = 0.4  # crossover probability
pMutation = 0.15  # mutation probability
selection_factor = 0.2  # if higher -> higher selection (more copies of better individuals)
elitarism_factor = 0.02
plans = []

filesize = os.path.getsize("bestIndividuals.txt")
if filesize != 0:
    readFromFile()
else:
    for i in range(numberOfIndividuals):
        plans.append(generatePlan())

bestIndividuals = []
bestPoints = []
for ep in range(numberOfEpochs):
    print(ep)
    elitePlans = []
    elitePoints = []
    points = []
    tmp = []
    if ep == 0:
        for pl in range(numberOfIndividuals):
            tmp.append(checkFitness(plans[pl], True))
        print("learning...")
    for pl in range(numberOfIndividuals):
        points.append(checkFitness(plans[pl], False))
    top10(plans, points)

    plans = reproduction(plans, points)
    plans = crossover(plans)
    if ep < 15:
        plans = mutation(plans)
    else:
        plans = laterMutation(plans)

    points = []
    for pl in range(numberOfIndividuals):
        points.append(checkFitness(plans[pl], False))
    plans, points = sort(plans, points)
    for i in range(int(numberOfIndividuals * elitarism_factor)):
        plans[i] = elitePlans[i]
    pMutation -= 0.0001

    for pl in range(numberOfIndividuals):
        points.append(checkFitness(plans[pl], False))
    plans, points = sort(plans, points)

    elitePoints = []
    for pl in range(int(numberOfIndividuals * elitarism_factor)):
        elitePoints.append(checkFitness(elitePlans[pl], False))
    print(elitePoints)

    if ep % 1 == 0:
        saveToFile()
        print(planToString(elitePlans[0]))
sort(plans, points)
bestPlansForClasses = plansForClasses(plans[99])
for bestPl in bestPlansForClasses:
    print(planToString(bestPl))
    print("~---##########################################################---~")
print("\n")
checkFitness(plans[99], True)

saveToFile()