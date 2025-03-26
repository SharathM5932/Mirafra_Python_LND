import random
import time
import threading
import pygame
import sys
import logging


# Configure logging
logging.basicConfig(
    filename="traffic_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
def log_event(message):
    logging.info(message)


# Default values of signal timers
defaultGreen = {0: 10, 1: 10, 2: 10, 3: 10}
defaultRed = 150
defaultYellow = 2

signals = []
noOfSignals = 4
currentGreen = 0  # Indicates which signal is green currently
nextGreen = 0  # Indicates which signal will turn green next
currentYellow = 0  # Indicates whether yellow signal is on or off

speeds = {'car': 2.25, 'bus': 1.8, 'truck': 1.8, 'bike': 2.5, 'ambulance': 3.5}  # average speeds of vehicles
ambulance_car = None

# Coordinates of vehicles' start
x = {'right': [0, 0, 0], 'down': [785, 757, 727], 'left': [1400, 1400, 1400], 'up': [587, 592, 642]}
y = {'right': [338, 360, 388], 'down': [0, 0, 0], 'left': [531, 501, 471], 'up': [800, 800, 800]}

vehicles = {'right': {0: [], 1: [], 2: [], 'crossed': 0}, 'down': {0: [], 1: [], 2: [], 'crossed': 0},
            'left': {0: [], 1: [], 2: [], 'crossed': 0}, 'up': {0: [], 1: [], 2: [], 'crossed': 0}}
vehicleTypes = {0: 'car', 1: 'bus', 2: 'truck', 3: 'bike', 4: 'ambulance'}
directionNumbers = {0: 'right', 1: 'down', 2: 'left', 3: 'up'}

# Coordinates of signal image, timer, and vehicle count
signalCoods = [(530, 230), (810, 230), (810, 570), (530, 570)]
signalTimerCoods = [(530, 210), (810, 210), (810, 550), (530, 550)]

# Coordinates of stop lines
stopLines = {'right': 590, 'down': 330, 'left': 800, 'up': 535}
defaultStop = {'right': 580, 'down': 320, 'left': 810, 'up': 545}

# Gap between vehicles
stoppingGap = 15  # stopping gap
movingGap = 15  # moving gap

pygame.init()
simulation = pygame.sprite.Group()

# Accident detection variables
ambulance_present = False

class TrafficSignal:
    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green
        self.signalText = ""


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, lane, vehicleClass, direction_number, direction):
        pygame.sprite.Sprite.__init__(self)
        self.lane = lane
        self.vehicleClass = vehicleClass
        self.speed = speeds[vehicleClass]
        self.direction_number = direction_number
        self.direction = direction
        self.x = x[direction][lane]
        self.y = y[direction][lane]
        self.crossed = 0
        vehicles[direction][lane].append(self)
        self.index = len(vehicles[direction][lane]) - 1
        path = "images/" + direction + "/" + vehicleClass + ".png"
        self.image = pygame.image.load(path)

        if (len(vehicles[direction][lane]) > 1 and vehicles[direction][lane][
            self.index - 1].crossed == 0):  # if more than 1 vehicle in the lane of vehicle before it has crossed stop line
            if (direction == 'right'):
                self.stop = vehicles[direction][lane][self.index - 1].stop - vehicles[direction][lane][
                    self.index - 1].image.get_rect().width - stoppingGap  # setting stop coordinate as: stop coordinate of next vehicle - width of next vehicle - gap
            elif (direction == 'left'):
                self.stop = vehicles[direction][lane][self.index - 1].stop + vehicles[direction][lane][
                    self.index - 1].image.get_rect().width + stoppingGap
            elif (direction == 'down'):
                self.stop = vehicles[direction][lane][self.index - 1].stop - vehicles[direction][lane][
                    self.index - 1].image.get_rect().height - stoppingGap
            elif (direction == 'up'):
                self.stop = vehicles[direction][lane][self.index - 1].stop + vehicles[direction][lane][
                    self.index - 1].image.get_rect().height + stoppingGap
        else:
            self.stop = defaultStop[direction]

        # Set new starting and stopping coordinate
        if (direction == 'right'):
            temp = self.image.get_rect().width + stoppingGap
            x[direction][lane] -= temp
        elif (direction == 'left'):
            temp = self.image.get_rect().width + stoppingGap
            x[direction][lane] += temp
        elif (direction == 'down'):
            temp = self.image.get_rect().height + stoppingGap
            y[direction][lane] -= temp
        elif (direction == 'up'):
            temp = self.image.get_rect().height + stoppingGap
            y[direction][lane] += temp
        simulation.add(self)

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if (self.direction == 'right'):
            if (self.crossed == 0 and self.x + self.image.get_rect().width > stopLines[
                self.direction]):  # if the image has crossed stop line now
                self.crossed = 1
            if ((self.x + self.image.get_rect().width <= self.stop or self.crossed == 1 or (
                    currentGreen == 0 and currentYellow == 0)) and (
                    self.index == 0 or self.x + self.image.get_rect().width < (
                    vehicles[self.direction][self.lane][self.index - 1].x - movingGap))):
                self.x += self.speed
        elif (self.direction == 'down'):
            if (self.crossed == 0 and self.y + self.image.get_rect().height > stopLines[self.direction]):
                self.crossed = 1
            if ((self.y + self.image.get_rect().height <= self.stop or self.crossed == 1 or (
                    currentGreen == 1 and currentYellow == 0)) and (
                    self.index == 0 or self.y + self.image.get_rect().height < (
                    vehicles[self.direction][self.lane][self.index - 1].y - movingGap))):
                self.y += self.speed
        elif (self.direction == 'left'):
            if (self.crossed == 0 and self.x < stopLines[self.direction]):
                self.crossed = 1
            if ((self.x >= self.stop or self.crossed == 1 or (currentGreen == 2 and currentYellow == 0)) and (
                    self.index == 0 or self.x > (
                    vehicles[self.direction][self.lane][self.index - 1].x + vehicles[self.direction][self.lane][
                self.index - 1].image.get_rect().width + movingGap))):
                self.x -= self.speed
        elif (self.direction == 'up'):
            if (self.crossed == 0 and self.y < stopLines[self.direction]):
                self.crossed = 1
            if ((self.y >= self.stop or self.crossed == 1 or (currentGreen == 3 and currentYellow == 0)) and (
                    self.index == 0 or self.y > (
                    vehicles[self.direction][self.lane][self.index - 1].y + vehicles[self.direction][self.lane][
                self.index - 1].image.get_rect().height + movingGap))):
                self.y -= self.speed


# Initialization of signals with default values
def initialize():
    ts1 = TrafficSignal(0, defaultYellow, defaultGreen[0])
    signals.append(ts1)
    ts2 = TrafficSignal(ts1.red + ts1.yellow + ts1.green, defaultYellow, defaultGreen[1])
    signals.append(ts2)
    ts3 = TrafficSignal(defaultRed, defaultYellow, defaultGreen[2])
    signals.append(ts3)
    ts4 = TrafficSignal(defaultRed, defaultYellow, defaultGreen[3])
    signals.append(ts4)
    repeat()

def repeat():
    global currentGreen, currentYellow, nextGreen, ambulance_present

    while True:
        # Check if an ambulance is present in any lane
        ambulance_present = False
        for direction in vehicles:
            for lane in range(3):  # Check all 3 lanes
                for vehicle in vehicles[direction][lane]:
                    if vehicle.vehicleClass == 'ambulance' and vehicle.crossed == 0:
                        ambulance_present = True
                        ambulance_direction = direction
                        break
                if ambulance_present:
                    break
            if ambulance_present:
                break

        # If ambulance is present, prioritize its lane
        if ambulance_present:
            # Find the signal index for the ambulance's direction
            for i in range(noOfSignals):
                if directionNumbers[i] == ambulance_direction:
                    currentGreen = i
                    nextGreen = (currentGreen + 1) % noOfSignals
                    break

            # Set all other signals to red
            for i in range(noOfSignals):
                if i != currentGreen:
                    signals[i].red = 9999  # Arbitrarily large value to keep it red
                    signals[i].green = 0
                    signals[i].yellow = 0

            # Wait until the ambulance crosses the stop line
            while ambulance_present:
                updateValues()
                time.sleep(1)
                # Re-check if the ambulance has crossed the stop line
                ambulance_present = False
                for vehicle in vehicles[ambulance_direction][lane]:
                    if vehicle.vehicleClass == 'ambulance' and vehicle.crossed == 0:
                        ambulance_present = True
                        break

            # After ambulance crosses, introduce a 5-second yellow light delay
            currentYellow = 1  # Set yellow signal on
            signals[currentGreen].yellow = 5  # Set yellow timer to 5 seconds

            while signals[currentGreen].yellow > 0:  # Wait for yellow timer to expire
                updateValues()
                time.sleep(1)

            currentYellow = 0  # Set yellow signal off

            # Reset signal timers to default values
            for i in range(noOfSignals):
                signals[i].red = defaultRed
                signals[i].green = defaultGreen[i]
                signals[i].yellow = defaultYellow
            log_event(f"Priority override: Ambulance detected at direction {direction} at {time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Normal signal cycle based on density
        else:

            # Find the lane with the highest vehicle count
            max_count = max(vehicle_counts.values())
            nextGreen = [key for key, value in vehicle_counts.items() if value == max_count][0]

            # Set the green signal for the lane with the highest count
            currentGreen = nextGreen

            # Reset the red timer for the next signal
            signals[nextGreen].red = defaultRed

            while (signals[currentGreen].green > 0):  # while the timer of current green signal is not zero
                updateValues()
                time.sleep(1)
            currentYellow = 1  # set yellow signal on

            # Reset stop coordinates of lanes and vehicles
            for i in range(0, 3):
                for vehicle in vehicles[directionNumbers[currentGreen]][i]:
                    vehicle.stop = defaultStop[directionNumbers[currentGreen]]

            while (signals[currentGreen].yellow > 0):  # while the timer of current yellow signal is not zero
                updateValues()
                time.sleep(1)
            currentYellow = 0  # set yellow signal off

            # Reset all signal times of current signal to default times
            signals[currentGreen].green = defaultGreen[currentGreen]
            signals[currentGreen].yellow = defaultYellow
            signals[currentGreen].red = defaultRed

            # Update the next green signal to the lane with the next highest count
            vehicle_counts[currentGreen] = 0  # Reset the count for the current green lane


# Update values of the signal timers after every second
def updateValues():
    for i in range(0, noOfSignals):
        if (i == currentGreen):
            if (currentYellow == 0):
                signals[i].green = max(0, signals[i].green - 1)  # Ensure green timer doesn't go negative
            else:
                signals[i].yellow = max(0, signals[i].yellow - 1)  # Ensure yellow timer doesn't go negative
        else:
            signals[i].red = max(0, signals[i].red - 1)  # Ensure red timer doesn't go negative
            # log_event(f"Signal {i} red timer: {signals[i].red}")

vehicle_counts = {0: 0, 1: 0, 2: 0, 3: 0}
max_vehicles = 50
ambulance_count = 0
last_ambulance_time = 0
v_count=0

# Generating vehicles in the simulation
def generateVehicles():
    global ambulance_present, ambulance_count, last_ambulance_time,v_count
    while True:
        vehicle_type = random.randint(0, 4)
        lane_number = random.randint(1, 2)
        temp = random.randint(0, 99)
        direction_number = 0
        dist = [25, 50, 75, 100]
        if (temp < dist[0]):
            direction_number = 0
        elif (temp < dist[1]):
            direction_number = 1
        elif (temp < dist[2]):
            direction_number = 2
        elif (temp < dist[3]):
            direction_number = 3

        current_time = time.time()

        if vehicle_type == 4:
            #log_event(f"Ambulance detected at direction {direction_number}, lane {lane_number}. Switching priority.")
            if ambulance_count >= 3:
                continue
            if ambulance_count > 0 and (current_time - last_ambulance_time < 30):
                continue
            # if vehicles[direction_number]['crossed']==1:
            #     ambulance_present=False
            #     passed_time = time.strftime('%Y-%m-%d %H:%M:%S')
            #     log_event(f"ambulance passed {passed_time}")

            ambulance_present = True
            #log_event(f"Ambulance detected at direction {direction_number}, lane {lane_number}. Switching priority.")
            ambulance_count += 1
            last_ambulance_time = current_time


        # else:
        #     log_event(f"{vehicleTypes[vehicle_type]} generated at direction {direction_number}, lane {lane_number}")

        Vehicle(lane_number, vehicleTypes[vehicle_type], direction_number, directionNumbers[direction_number])
        vehicle_counts[direction_number] += 1
        print(vehicle_counts)
        time.sleep(1)
        # v_count+=1

class Main:
    thread1 = threading.Thread(name="initialization", target=initialize, args=())  # initialization
    thread1.daemon = True
    thread1.start()

    # Colours
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Screensize
    screenWidth = 1400
    screenHeight = 800
    screenSize = (screenWidth, screenHeight)

    # Setting background image i.e. image of intersection
    background = pygame.image.load('images/grassbg.png')
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("SIMULATION")

    # Loading signal images and font
    redSignal = pygame.image.load('images/signals/red.png')
    yellowSignal = pygame.image.load('images/signals/yellow.png')
    greenSignal = pygame.image.load('images/signals/green.png')
    font = pygame.font.Font(None, 30)

    thread2 = threading.Thread(name="generateVehicles", target=generateVehicles, args=())  # Generating vehicles
    thread2.daemon = True
    thread2.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    log_event(f"exited".center(50,'-'))
                    sys.exit()

        screen.blit(background, (0, 0))  # display background in simulation
        for i in range(0, noOfSignals):  # display signal and set timer according to current status: green, yellow, or red
            if (i == currentGreen):
                if (currentYellow == 1):
                    signals[i].signalText = signals[i].yellow
                    screen.blit(yellowSignal, signalCoods[i])
                else:
                    signals[i].signalText = signals[i].green
                    screen.blit(greenSignal, signalCoods[i])
            else:
                if (signals[i].red <= 10):
                    signals[i].signalText = signals[i].red
                else:
                    signals[i].signalText = "---"
                screen.blit(redSignal, signalCoods[i])
        signalTexts = ["", "", "", ""]

        # display signal timer
        for i in range(0, noOfSignals):
            signalTexts[i] = font.render(str(signals[i].signalText), True, white, black)
            screen.blit(signalTexts[i], signalTimerCoods[i])

        # display the vehicles
        for vehicle in simulation:
            screen.blit(vehicle.image, [vehicle.x, vehicle.y])
            vehicle.move()
        pygame.display.update()

Main()
