
from tkinter.constants import TRUE


PC_DEV = True

"""
Monitor Details
"""

BG_COLOR = 'black'          # Background Color
FONT_COLOR = 'white'        # changes color of all text
TIMEZONE = 'US/Eastern'     # set timezone Replace with 'Africa/Accra'

"""
Pin Assignments
"""

# ambient temp not explicitly written DTMP_PI = 21
PIN_SNOOZE_BTN = 22 #40               # Snooze Button
PIN_ALARM_LED = 12 #32
PIN_PREHEAT_BTN = 5 #29
PIN_PREHEAT_LED = 16 #36
PIN_HEATER_CHECK_1 = 24 #18
PIN_HEATER_CHECK_2 = 25 #22
PIN_HEATER_CHECK_3 = 8 #24
PIN_HEATER_CHECK_4 = 7 #26
PIN_THERM_IN = 17 #11
PIN_THERM_OUT = 23 #16
PIN_SET_POINT_CMPR = 19 #35
PIN_CTRL_SNSR_CMPR = 6 #31
PIN_ALARM_PWM = 10 #19 ; ; 18 #12
PIN_ADC_PWM = 13 #33
PIN_HEAT_CTRL = 21 #37

"""
Skin Temperature Settings in Sensor.py
"""
DIGITAL_VOLTAGE = 3.3

# PWM Settings
ADC_VOLTAGE_LOWER = 0.3000   # starting range for skin temperature
ADC_VOLTAGE_UPPER =   0.3800   # Ending range for skin temperature
ADC_SEARCH_CYCLES = 5


ADC_START_VOLTAGE = 0.28
ADC_END_VOLTAGE = 0.40

# Warning Settings
SKIN_TEMP_THRES_MAX = 39    # Minimum Skin Temperature Threshold Value
SKIN_TEMP_THRES_MIN = 20    # Maximum Skin Temperature Threshold Value
#TODO: these values need to be double checked
AMB_TEMP_THRES_MIN = 30     # Minimum Ambient(Incubator) Temperture Threshold Value
AMB_TEMP_THRES_MAX = 40     # Maximum Ambient(Incubator) Temperture Threshold Value
CONTROL_THRESHOLD = 2
ALARM_THRESHOLD = 4


"""
Speaker Settings
"""

SPKR_FREQ = 2000            # Frequency of the speaker sound
SNOOZE_LENGTH = 120         # Indicates how long the snooze button should last (in seconds)

